#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics
"""
from sys import stdin
import re


def count_occurrences(input_list, target):
    count = 0
    for item in input_list:
        if item == target:
            count += 1
    return count


def stat_dict(lst, hash_table):
    for item in lst:
        count = count_occurrences(lst, item)
        hash_table[item] = count
    return hash_table


def stats():
    requests = []
    status_codes = []
    stat_count = {}
    file_size = 0

    try:
        for line in stdin:
            pattern = line.split()
            status_code = pattern[-2]
            status_codes.append(status_code)
            file_size += int(pattern[-1])

            if len(status_codes) % 10 == 0:
                status_codes.sort()
                stat_count = stat_dict(status_codes, stat_count)
                print("File size: {}".format(file_size))
                for k, v in stat_count.items():
                    print("{}: {}".format(k, v))

    except KeyboardInterrupt:
        status_codes.sort()
        stat_count = stat_dict(status_codes, stat_count)
        print("File size: {}".format(file_size))
        for k, v in stat_count.items():
            print("{}: {}".format(k, v))


if __name__ == '__main__':
    stats()
