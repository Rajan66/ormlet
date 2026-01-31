from examples.models.food import Food


class RetrieveQueryService:
    def __init__(self) -> None:
        pass

    def start(self):
        self._run()

    def _run(self):
        results = Food.objects.all()

        print("Query result:")

        for row in results:
            print(row)
