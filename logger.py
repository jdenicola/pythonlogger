#!/usr/bin/python3

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

class LocalLogger:
    def __init__(self, log_file, log_name, loglevel='debug', max_bytes=200000, max_files=10):
        """
        Uso:
        # logger.debug('mensaje debug')
        # log.info('mensaje info')
        # log.warning('mensaje warning')
        # log.error('mensaje error')
        # log.critical('mensaje critical')
        """
        self.log_file = str(Path(__file__).resolve().parent)

        self.__logger = logging.getLogger(log_name)
        fh = RotatingFileHandler(log_file, max_bytes, max_files)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fh.setFormatter(formatter)
        self.__logger.addHandler(fh)
    
    def SetLevel(self, level):
        if level == "debug":
            self.__logger.setLevel(logging.DEBUG)
        if level == "info":
            self.__logger.setLevel(logging.INFO)
        if level == "warning":
            self.__logger.setLevel(logging.WARNING)
        if level == "error":
            self.__logger.setLevel(logging.ERROR)
        if level == "critical":
            self.__logger.setLevel(logging.CRITICAL)

    def debug(self, message):
        self.__logger.debug(message)
    
    def info(self, message):
        self.__logger.info(message)

    def warning(self, message):
        self.__logger.warning(message)

    def error(self, message):
        self.__logger.error(message)

    def critical(self, message):
        self.__logger.critical(message)
