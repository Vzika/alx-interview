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

# #!/usr/bin/env python4
# def validUTF8(data):
#     # Traverse the given array
#     # find the num of bytes of each number, by calculating the number of leading 1s.
#     # check if the next n - 1 bytes start with 10, if not return False, else return True
    
#     # a character in UTF-8 can be from 1 - 4 bytes, subjected to the following rules:
#     # 1. for 1-byte character, the first bit is a 0, followed by its Unicode code
#     # 2. for n-bytes character, the first n-bits are all ones, the n+1 bit is 0, followed by n-1 bytes
#     # with most significant 2 bits being 10
#     #Each byte is an 8-bit number, which means it can have a value from 0 to 255 (since 2^8 = 256, the possible values range from 0 to 255).

#     #utf-8 is a variable width character encoding, capable of encoding unicode characters
 
#    #197
 
#    #7   6  5  4  3  2  1 0
#    #128 64 32 16 8  4  2 1
#    #1   1   0  0 0  1  0 1
#    #A valid byte in UTF-8 should be in the range 0 to 255.
#    #
# If any value in the data list is greater than 255, it means that value cannot be a valid byte in UTF-8 encoding.

#     i = 0
#     while i < len(data):
#         numof_byte = 0
#         val = data[i]

#         # Check if the byte value is out of range
#         if val > 255:
#             return False

#         # Determine the number of bytes in the current UTF-8 character
#         if val & 128 == 0:  # 1-byte character (ASCII)
#             numof_byte = 1
#         elif val & 224 == 192:  # 2-byte character
#             numof_byte = 2
#         elif val & 240 == 224:  # 3-byte character
#             numof_byte = 3
#         elif val & 248 == 240:  # 4-byte character
#             numof_byte = 4
#         else:
#             return False

#         # Check if the subsequent bytes are valid continuation bytes
#         for j in range(1, numof_byte):
#             if i + j >= len(data):
#                 return False
#             elif data[i + j] & 192 != 128:
#                 return False

#         # Move to the next character in the data
#         i += numof_byte

#     return True

# # Main file for testing
# if __name__ == "__main__":
#     data = [65]
#     print(validUTF8(data))  # True

#     data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
#     print(validUTF8(data))  # True

#     data = [229, 65, 127, 256]
#     print(validUTF8(data))  # False

