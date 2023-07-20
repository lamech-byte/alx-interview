#!/usr/bin/python3
import sys

def print_stats(file_sizes, status_codes):
    total_size = sum(file_sizes)
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def main():
    file_sizes = []
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            if count > 0 and count % 10 == 0:
                print_stats(file_sizes, status_codes)
            parts = line.split(" ")
            try:
                size = int(parts[-1])
                status_code = int(parts[-2])
                file_sizes.append(size)
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except ValueError:
                pass
    except KeyboardInterrupt:
        pass

    print_stats(file_sizes, status_codes)

if __name__ == "__main__":
    main()
