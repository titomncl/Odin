import logging
import sys
import os

from logging.handlers import TimedRotatingFileHandler

from Odin.source.common import make_dirs, concat


def log(name):

    log_path = concat(os.path.expanduser('~').replace("\\", "/"), ".logs", name, separator="/")
    make_dirs(log_path)

    logger = logging.getLogger(name)
    logger.handlers = list()
    logger.setLevel(logging.DEBUG)

    date_format = "%Y-%m-%d %H:%M:%S"

    file_formatter = logging.Formatter('%(asctime)s -- [%(levelname)s] -- %(message)s', datefmt=date_format)
    file_handler = TimedRotatingFileHandler(filename="{}/{}.log".format(log_path, name),
                                            when="midnight", backupCount=7, encoding="utf-8")
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)

    stdout_handler = logging.StreamHandler(sys.stdout)
    console_formatter = logging.Formatter('%(asctime)s -- %(levelname)s -- %(message)s', datefmt=date_format)
    stdout_handler.setFormatter(console_formatter)
    stdout_handler.setLevel(logging.DEBUG)
    logger.addHandler(stdout_handler)

    sys.stderr = StreamToLogger(logger, sys.stderr, logging.ERROR)

    return logger


class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, stream=sys.stdout, log_level=logging.INFO):
        self.logger = logger
        self.stream = stream
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        self.stream.write(buf)
        # self.logger.log(self.log_level, repr(buf))
        self.linebuf += buf
        if buf == '\n':
            self.flush()

    def flush(self):
        # Flush all handlers
        for line in self.linebuf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())
        self.linebuf = ''
        self.stream.flush()
        for handler in self.logger.handlers:
            handler.flush()
