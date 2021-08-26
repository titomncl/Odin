import logging
import os
import sys

try:
    from typing import TextIO
except ImportError:
    pass

from logging.handlers import TimedRotatingFileHandler

from .common import concat, make_dirs


def log(name):
    # type: (str) -> logging.Logger
    """.

    Args:
        name: name to the log

    Returns:
        Logger object to interact with the logger

    """
    log_path = concat(os.path.expanduser("~").replace("\\", "/"), ".logs", name, separator="/")
    make_dirs(log_path)

    logger = logging.getLogger(name)
    logger.handlers = list()
    logger.setLevel(logging.DEBUG)

    date_format = "%Y-%m-%d %H:%M:%S"

    file_formatter = logging.Formatter("%(asctime)s -- [%(levelname)s] -- %(message)s", datefmt=date_format)
    file_handler = TimedRotatingFileHandler(
        filename="{}/{}.log".format(log_path, name), when="midnight", backupCount=7, encoding="utf-8"
    )
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)

    stdout_handler = logging.StreamHandler(sys.stdout)
    console_formatter = logging.Formatter("%(asctime)s -- %(levelname)s -- %(message)s", datefmt=date_format)
    stdout_handler.setFormatter(console_formatter)
    stdout_handler.setLevel(logging.DEBUG)
    logger.addHandler(stdout_handler)

    sys.stderr = StreamToLogger(logger, sys.stderr, logging.ERROR)

    return logger


class StreamToLogger(object):
    """Fake file-like stream object that redirects writes to a logger instance."""

    def __init__(self, logger, stream=sys.stdout, log_level=logging.INFO):
        # type: (logging.Logger, TextIO, int) -> None
        self.logger = logger
        self.stream = stream
        self.log_level = log_level
        self.linebuf = ""

    def write(self, buf):
        # type: (str) -> None
        self.stream.write(buf)
        self.linebuf += buf
        if buf == "\n":
            self.flush()

    def flush(self):
        # Flush all handlers
        for line in self.linebuf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())
        self.linebuf = ""
        self.stream.flush()
        for handler in self.logger.handlers:
            handler.flush()
