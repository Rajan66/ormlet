# ORMlet Code Audit Findings

**Branch:** `main`  
**Date:** 2026-11-08  
**Scope:** All Python files in the repository

---

## 🔴 Critical — Security

### 1. SQL Injection in `QuerySet.get()`

**File:** `managers/queryset.py:24`

```python
query += f"{key}='{value}'"
```

Both the column name (`key`) and value are interpolated directly into the SQL string. An attacker can break out of the quotes and execute arbitrary SQL.

Example injection:

```python
Food.objects.get(name="' ; DROP TABLE food; --")
```

Produces:

```sql
SELECT * FROM food WHERE name=''; DROP TABLE food; --';
```

**Fix:** Use parameterized queries (`%s` placeholders with values passed separately to `cursor.execute()`). Quote identifiers (table/column names) with `psycopg.sql.Identifier`.

---

### 2. SQL Injection in `ModelHelper.get_column_constraints()`

**File:** `helpers/model.py:15-30`

Constraint fragments are built by concatenating raw field values into DDL:

```python
if key == "default" and value:
    constraints += f"DEFAULT {value}"

constraints += f"CHECK (LENGTH({field})>={value})"
```

If a field `default` were ever user-controlled, it could inject SQL into `CREATE TABLE`. String defaults also produce invalid SQL (e.g., `DEFAULT active` instead of `DEFAULT 'active'`).

**Fix:** Validate/quote values before embedding in DDL, or restrict defaults to safe literal forms.

---

### 3. Unsafe DDL Construction in `ModelManager.create_table()`

**File:** `managers/db.py:29`

```python
columns.append(
    f"{col_name} {field_obj.get_column_type()} {constraints}"
)
```

Column names and constraint fragments are concatenated raw. While current sources are trusted (model field definitions), this is a vector if any part becomes dynamic/user-controlled.

**Fix:** Use `psycopg.sql.Identifier` for column/table names and `sql.SQL`/`sql.Literal` for values.

---

### 4. Unsafe Table Name Interpolation in `Manager.get()` / `Manager.all()`

**File:** `managers/manager.py:22-24`

```python
res = connection.cursor.execute(
    sql.SQL(queryset % self.model._tablename)
)
```

This mixes `%` string formatting with `sql.SQL()`. Table names should be quoted as identifiers via `psycopg.sql.Identifier`, not string-formatted.

---

## 🟠 High — Correctness / Logic Bugs

### 5. Broken AND logic in `QuerySet.get()` — RESOLVED

**File:** `managers/queryset.py:22`

Was `if index > 1:` (skipped `AND` between the first two conditions). Now `if index >= 1:`, so all subsequent conditions are joined correctly.

Example: `get(name="momo", origin="nepal")` now produces:

```sql
WHERE name='momo' AND origin='nepal'
```

**Status:** Fixed in working tree.

---

### 6. Invalid SQL when model has no fields

**File:** `managers/queryset.py:33-39`

If `_fields` is empty, `fields` stays `""`, generating:

```sql
SELECT  FROM %s;
```

Also uses `__len__()` directly instead of `len()`.

---

### 7. Meaningless guard in `ModelHelper`

**File:** `helpers/model.py:16`

```python
for key, value in field_obj.__dict__.items():
    if key is not None:
```

`key` is always a string from `__dict__.items()`, so this check does nothing. It likely should guard on `value`.

---

### 8. `get_column_type()` returns a StrEnum member, not a `str`

**File:** `models/fields/base.py:33` (uncommitted change)

```python
return DatabaseDataType[self.get_internal_type()]
```

Returns the `DatabaseDataType` enum member instead of `.value`. It works by accident inside f-strings (StrEnum `__str__` returns the value), but breaks the type contract — callers expect `str`.

**Fix:** Revert to `.value`:

```python
return DatabaseDataType[self.get_internal_type()].value
```

---

### 9. No primary key / `id` column

No model defines an auto-incrementing primary key. You cannot reliably `get(id=...)` or reference specific rows.

---

### 10. No `save()` / `create()` / `insert()` method

You can create tables and read rows, but there is no way to write data into the database.

---

### 11. Queries return raw tuples, not model instances

**File:** `managers/manager.py:26, 41`

`fetchone()` / `fetchall()` return raw DB rows. There is no hydration into `Model` objects.

---

## 🟡 Medium — Design & Robustness

### 12. New connection per operation

`Manager.get()`, `Manager.all()`, and `ModelManager.create_table()` each open a brand-new Postgres connection via `ConnectionManager`. This is fine for a learning toy but incurs TCP/auth latency on every call and can exhaust Postgres `max_connections` under load.

**Suggestion:** Use `psycopg_pool.ConnectionPool` once you move beyond scripts.

### 13. No rollback on error / cursor not closed

**File:** `base/connection.py:30-32`

`ConnectionManager.__exit__` closes the connection but never calls `rollback()` on exception, and never explicitly closes the cursor.

### 14. No `filter()`, `exclude()`, `order_by()`, `limit()`

Only `get()` and `all()` exist. The ORM cannot do partial or ordered retrieval.

### 15. `db_index` is stored but never acted upon

**File:** `models/fields/base.py:27`

The field accepts `db_index` but no code creates indexes from it.

### 16. Config hard-fails at import time

**File:** `base/env_config.py:40-46`

If `.env` is missing or malformed, importing `base` raises `RuntimeError` immediately.

---

## 🟢 Low / Quality

### 17. No tests

There is no test directory or test file.

### 18. Uncommitted changes in progress

`base/data_type.py` and `models/fields/base.py` have unstaged StrEnum modifications that are not finished or committed.

### 19. Example will fail

**File:** `examples/query/retrieve.py:15`

`Food.objects.get(name="momo", origin="nepal")` still hits bug #1 (no parameterization); bug #5 (missing `AND`) is fixed.

### 20. `__len__()` instead of `len()`

**File:** `managers/queryset.py:34`

Unidiomatic but not a bug.

---

## Recommended Fix Order

1. **Parameterize all queries** — `QuerySet.get()` and `all()` should use `%s` placeholders and pass values to `cursor.execute()`. Use `psycopg.sql.Identifier` for table/column names.
2. **Fix the `AND` bug** in `QuerySet.get()` (`index > 0`).
3. **Revert `get_column_type()`** to return `.value` (plain `str`).
4. **Add a primary key (`id`)** to models.
5. **Add `save()` / `create()`** so you can write data.
6. **Hydrate results** into `Model` instances instead of raw tuples.
