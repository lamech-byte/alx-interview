#!/usr/bin/python3
"""
    Print statistics based on file sizes and status codes.

    Args:
        file_sizes (list): List of file sizes.
        status_codes (dict): Dictionary of status codes and their occurrences.
    """
import sys


def print_stats(file_sizes, status_codes):
    """
    Print statistics based on file sizes and status codes.

    Args:
        file_sizes (list): List of file sizes.
        status_codes (dict): Dictionary of status codes and their occurrences.
    """
    total_size = sum(file_sizes)
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    """
    Read stdin line by line, compute metrics, and print statistics.
    """
    file_sizes = []
    status_codes = {
        200: 0,
        301: 0,
        400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split(" ")
            if len(parts) < 9:
                continue
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
