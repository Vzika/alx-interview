#!/usr/bin/python3
"""UTF8 validation.
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """check if data set represents a valid UTF-8 encoding
"""
    i = 0
    while i < len(data):
        leading_byte = data[i]
        if leading_byte >> 7 & 1 == 0:
            bytes = 1
        elif leading_byte >> 5 & 1 == 0:
            bytes = 2
        elif leading_byte >> 4 & 1 == 0:
            bytes = 3
        elif leading_byte >> 3 & 1 == 0:
            bytes = 4
        else:
            return False

        if i + bytes > len(data):
            return False

        for j in range(1, bytes):
            if (data[i + j] >> 6 & 1) != 0:
                return False

        i += bytes
    return True


# Testing file
# data = [65]
# print(validUTF8(data))
#
# data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
# print(validUTF8(data))
#
# data = [229, 65, 127, 256]
# print(validUTF8(data))
