import logging
import os
from logging.handlers import TimedRotatingFileHandler
from configuration.config import config


class Logger:
    def __init__(self, prefix: str = None):
        self.prefix = prefix or config["logging"]["default_prefix"]
        self.logger = logging.getLogger(self.prefix)
        if not self.logger.hasHandlers():
            self.logger.setLevel(logging.DEBUG)

            log_format = "%(asctime)s - "
            if self.prefix:
                log_format += f"[{self.prefix}] - "
            log_format += "[%(filename)s] [%(funcName)s] - %(levelname)s - %(message)s"

            formatter = logging.Formatter(log_format)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            logging_config = config["logging"]
            log_directory = os.path.dirname(
                logging_config.get("file_path", "logs/app.log")
            )
            if not os.path.exists(log_directory):
                os.makedirs(log_directory)

            timed_rotating_handler = TimedRotatingFileHandler(
                logging_config.get("file_path", "logs/app.log"),
                when=logging_config.get("when", "w0"),
                interval=logging_config.get("interval", 1),
                backupCount=logging_config.get("backupCount", 4),
            )
            timed_rotating_handler.setFormatter(formatter)

            self.logger.addHandler(console_handler)
            self.logger.addHandler(timed_rotating_handler)
