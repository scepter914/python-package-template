import datetime
import logging
import os

from package_name.util.file import format_time
from pythonjsonlogger import jsonlogger


def CustomTextFormatter():
    """[summary]
    Custom Formatter for text
    """
    return logging.Formatter(
        "[%(asctime)2s] [%(levelname)7s] [%(filename)s:%(lineno)d %(funcName)s] %(message)s"
    )


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """[summary]
    Custom Formatter for json
    """

    def parse(self):
        return [
            "timestamp",
            "level",
            "pathname",
            "lineno",
            "funcName",
            "message",
        ]

    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


class SensitiveWordFilter(logging.Filter):
    def filter(self, record):
        sensitive_words = [
            "password",
            "auth_token",
            "token",
            "secret",
        ]
        log_message = record.getMessage()
        for word in sensitive_words:
            if word in log_message:
                return False
        return True


def configure_logger(
    log_directory_path: str,
    log_file_name: str = "{Time}_log.txt",
    modname: str = "",
    console_log_level: int = logging.INFO,
    file_log_level: int = logging.DEBUG,
    log_format: str = "txt",
) -> logging.Logger:
    """
    Set logger

    Args:
        log_directory_path (str): The log directory path.
        log_file_name (str, optional): The log file name. Defaults to "{Time}_log.txt"
        console_log_level (int, optional): Log level for console. Defaults to logging.INFO.
        file_log_level (int, optional): Log level for log file. Defaults to logging.DEBUG.
        log_format (str, optional): Log format. Choose "txt" (default) or "json".

    Raises:
        NotImplementedError: Set "txt" or "json" in log_format

    Returns:
        logging.Logger: Logger class
    """

    # make directory
    os.makedirs(log_directory_path, exist_ok=True)

    if log_format == "txt":
        formatter = CustomTextFormatter()
    elif log_format == "json":
        formatter = CustomJsonFormatter()
    else:
        raise NotImplementedError

    logger: logging.Logger = logging.getLogger(modname)
    logger.addFilter(SensitiveWordFilter())
    logger.setLevel(console_log_level)

    # handler for console
    stream_handler: logging.StreamHandler = logging.StreamHandler()
    stream_handler.setLevel(console_log_level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # handler for file
    log_file_name = format_time(log_file_name)
    log_file_full_path: str = os.path.join(log_directory_path, log_file_name)
    file_handler: logging.FileHandler = logging.FileHandler(
        filename=log_file_full_path, encoding="utf-8"
    )
    file_handler.setLevel(file_log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
