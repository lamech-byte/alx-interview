#!/usr/bin/python3
"""
UTF-8 Validation Module
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing 1 byte of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """
    def get_num_bytes(byte):
        """
        Returns the number of bytes for a given UTF-8 character.
        """
        if byte & 0x80 == 0:       # 1 byte character
            return 1
        elif byte & 0xE0 == 0xC0:  # 2 byte character
            return 2
        elif byte & 0xF0 == 0xE0:  # 3 byte character
            return 3
        elif byte & 0xF8 == 0xF0:  # 4 byte character
            return 4
        return 0  # Invalid byte

    def check_next_bytes(start_idx, num_bytes):
        """
        Checks the next 'num_bytes' bytes to ensure they follow the pattern
        10xxxxxx.

        Args:
            start_idx (int): The index of the current byte in the 'data' list.
            num_bytes (int): The number of bytes to check.

        Returns:
            bool: True if the next 'num_bytes' bytes are valid, else return
            False.
        """
        for i in range(start_idx + 1, start_idx + num_bytes):
            if i >= len(data) or data[i] & 0xC0 != 0x80:
                return False
        return True

    idx = 0
    while idx < len(data):
        num_bytes = get_num_bytes(data[idx])

        # Invalid UTF-8 character: More bytes than needed
        if num_bytes == 0 or idx + num_bytes > len(data):
            return False

        # Check if the next bytes are valid
        if not check_next_bytes(idx, num_bytes - 1):
            return False

        # Invalid UTF-8 character: Value greater than 0x10FFFF
        if num_bytes == 4 and (data[idx] & 0x07) >= 0x05:
            return False

        idx += num_bytes

    return True


if __name__ == "__main__":
    # Test cases
    data = [65]
    print(validUTF8(data))  # True

    data = [
        80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33
    ]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False

    # Additional test cases
    data = [235, 140]
    print(validUTF8(data))  # False

    data = [345, 467]
    print(validUTF8(data))  # False
