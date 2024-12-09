#!/usr/bin/env python3
"""Obfuscates log data."""
import re


def filter_datum(fields, redaction, message, separator):
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
