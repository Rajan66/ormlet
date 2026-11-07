from examples.models.food import Food


class RetrieveQueryService:
    """Example service that queries Food and prints rows."""

    def __init__(self) -> None:
        pass

    def start(self):
        self._run()

    def _run(self):
        # results = Food.objects.all()
        result = Food.objects.get(name="momo", origin="nepal")

        print("Query result:", result)

        # for row in results:
        #     print(row)
