#!/usr/bin/env python3
"""Obfuscates log data."""
import re
import logging
from typing import List


import logging


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """
    Obfuscate specified fields in a log message.

    Args:
        field (list): Fields to obfuscate.
        redaction (str): Value to replace matched fields with.
        message (str): Log message to process.
        separator (str): Field separator in the log message.

    Returns:
       str: Log message with specified fields obfuscated.
    """
    pattern = r'({})=([^{}]*)'.format('|'.join(fields), re.escape(separator))
    return re.sub(pattern, r'\1=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    FORMAT_FIELDS = ('name', 'levelname', 'asctime', 'message')
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formats a LogRecord.
        """
        msg = super(RedactingFormatter, self).format(record)
        txt = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return txt
