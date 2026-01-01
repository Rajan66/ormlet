import logging


class BaseLogger:
    @staticmethod
    def configure():
        logging.basicConfig(
            level=logging.INFO,
            encoding="utf-8",
            format="[{asctime}] PID: {process:d} - [{levelname}] - {message}",  # noqa E501
            style="{",
            datefmt="%Y-%m-%d %H:%M",
        )
