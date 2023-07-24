#!/usr/bin/python3
"""
This script is a log parsing tool that reads stdin line by line,
computes metrics, and prints statistics based on file
sizes and status codes.
"""
import sys


def is_valid_log_line(line):
    """
    Check if the log line matches the specified format.

    Args:
        line (str): The log line to check.

    Returns:
        bool: True if the line is valid, False otherwise.
    """
    parts = line.split()
    return len(parts) >= 9 and parts[6] == '"GET' and parts[8].isdigit()


def print_stats(file_sizes, status_codes):
    # ... (rest of the function remains the same)


def main():
    # ... (rest of the function remains the same)

    try:
        for line in sys.stdin:
            count += 1
            if not is_valid_log_line(line):
                continue
            parts = line.split()
            try:
                size = int(parts[-1])
                status_code = int(parts[-2])
                file_sizes.append(size)
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except ValueError:
                pass
            if count > 0 and count % 10 == 0:
                print_stats(file_sizes, status_codes)

    except KeyboardInterrupt:
        pass

    print_stats(file_sizes, status_codes)


if __name__ == "__main__":
    main()
