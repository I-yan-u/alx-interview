#!/usr/bin/env python3
"""
Calculates the fewest number of
operations needed to result in exactly
n H characters in the file.
If in a text file, there is a single character H.
and your text editor can execute only two operations
in this file: Copy All and Paste
"""
from typing import List, Tuple


def copy(file: str, string: str, op: int) -> Tuple[str, str, int]:
    """ `Copy all` operation.
            `Args`:
                `file`(string): Source string to copy.\n
                `string`(string): Destination string to copy.\n
                `op`(int): number of operations.
        `Returns`: tuple of `file`, `string` and `op`.
    """
    string = file
    op += 1
    return file, string, op


def paste(file: str, string: str, op: int) -> Tuple[str, str, int]:
    """ `Paste` operation.
            `Args`:
                `file`(string): Destination string.\n
                `string`(string): Source string to paste.\n
                `op`(int): number of operations.
        `Returns`: tuple of `file`, `string` and `op`.
    """
    file += string
    op += 1
    return file, string, op


def factors(num: int) -> List[int]:
    """Returns a list of factors in the given number"""
    return [i for i in range(1, num+1) if num % i == 0]


def minOperations(n: int) -> int:
    """ minimum number of operations required """
    file = 'H'  # virtual file
    string = ''  # clipboard text
    operations = 0  # number of operations

    facts = factors(n)

    if n <= 0 or type(n) is not int:
        return 0

    if len(factors(n)) == 2:
        last_fact = factors(n)[-1]
        return last_fact

    elif len(factors(n)) > 2:
        file, string, operations = copy(file, string, operations)
        while len(file) < n:
            file, string, operations = paste(file, string, operations)
            if len(file) in facts and len(file) < n:
                file, string, operations = copy(file, string, operations)
                file, string, operations = paste(file, string, operations)
            elif len(file) == n:
                return operations
            else:
                continue
    return operations
