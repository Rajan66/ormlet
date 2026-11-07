from dataclasses import dataclass
from pathlib import Path

from dotenv import dotenv_values

BASE_DIR = Path(__file__).resolve().parents[1]
_raw = dotenv_values(BASE_DIR / ".env")


def require(key: str) -> str:
    """Read a required env var from .env; raise RuntimeError if missing."""
    value = _raw[key]
    if value is None:
        raise RuntimeError(f"Missing required env var: {key}")
    return value


@dataclass(frozen=True)
class Config:
    """
    Frozen dataclass of database settings loaded from .env at import time.
    """

    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DEBUG: bool


def _bool(value: str | None) -> bool:
    """Parse a string into a boolean; True for {"1","true","yes","on"}."""
    return value.lower() in {"1", "true", "yes", "on"} if value else False


# Singleton app config loaded from .env at import time. Every DB credential is
# required; require() raises RuntimeError if any is missing. DEBUG defaults to
# False when absent.
config = Config(
    DB_NAME=require("DB_NAME"),
    DB_USER=require("DB_USER"),
    DB_PASSWORD=require("DB_PASSWORD"),
    DB_HOST=require("DB_HOST"),
    DB_PORT=require("DB_PORT"),
    DEBUG=_bool(_raw.get("DEBUG")),
)
