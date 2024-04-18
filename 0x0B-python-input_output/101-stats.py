#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_stats(total_size, status_codes):
    """Print accumulated metrics.

    Args:
        total_size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("Total file size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("Status {}: {}".format(code, count))

def process_line(line, total_size, status_codes, valid_codes):
    """Process a line from input.

    Args:
        line (str): The line read from input.
        total_size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
        valid_codes (set): Set of valid status codes.
    """
    parts = line.split()
    if len(parts) >= 2:
        try:
            size = int(parts[-1])
            total_size += size
        except ValueError:
            pass

        if len(parts) >= 3:
            code = parts[-2]
            if code in valid_codes:
                status_codes[code] = status_codes.get(code, 0) + 1
    return total_size

if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_count = 0

    try:
        for line in sys.stdin:
            total_size = process_line(line, total_size, status_codes, valid_codes)
            line_count += 1
            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
