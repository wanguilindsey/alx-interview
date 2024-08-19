#!/usr/bin/python3
"""Check if a data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """Validate if the data is a valid UTF-8 encoding."""
    try:
        masked_data = [n & 255 for n in data]
        bytes(masked_data).decode("UTF-8")
        return True
    except Exception:
        return False
