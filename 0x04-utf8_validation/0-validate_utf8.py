#!/usr/bin/python3
"""
Validates a given dataset to be UTF-8 encoded
"""
from typing import List


def bin_check(integer: int) -> int:
    """
    convert to binary
    """
    bin = []
    a = integer
    count = 0
    final = False
    while a//2 != 0:
        a //= 2
        count += 1
    count += 1

    for _ in range(count):
        bin.append(integer % 2)
        integer //= 2

    if len(bin) > 8:
        bin.pop()

    for bit in bin:
        if bit == 1:
            final = True
    return final


def validUTF8(data: List[int]) -> bool:
    """
    UTF-8 validation
    """
    if not data:
        return False
    truthy = 1
    for intg in data:
        truthy *= bin_check(intg)
    return bool(truthy)
