import logging
import sys

from logging.handlers import TimedRotatingFileHandler

from Odin.source.common import make_dirs, concat


def log(name):

    make_dirs("logs")

    logger = logging.getLogger(name)
    logger.handlers = list()
    logger.setLevel(logging.DEBUG)

    date_format = "%Y-%m-%d %H:%M:%S"

    # sys.stderr = StreamToLogger(logger, sys.stderr, logging.ERROR)

    formatter = logging.Formatter('%(asctime)s -- %(levelname)s -- %(message)s', datefmt=date_format)

    file_handler = TimedRotatingFileHandler(filename=concat("logs/", name, ".log"),
                                            when="midnight", backupCount=7, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    stdout_handler.setLevel(logging.DEBUG)
    logger.addHandler(stdout_handler)

    # stderr_handler = logging.StreamHandler(sys.stderr)
    # stderr_handler.setFormatter(formatter)
    # stderr_handler.setLevel(logging.ERROR)
    # logger.addHandler(stderr_handler)

    # sys.stdout = StreamToLogger(logger, sys.stdout, logging.DEBUG)
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
