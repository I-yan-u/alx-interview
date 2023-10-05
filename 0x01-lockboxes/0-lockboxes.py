#!/usr/bin/python3
"""
0-lockboxes.py
Funcion(s): canUnlockAll(boxes: list) -> bool
"""


def evaluate_truthy(box: list) -> bool:
    """Converts a list of boolean into a boolean value.
        Args: List containing boolean values
        Returns: bool
    """
    final_bool = True
    for value in box:
        final_bool *= value

    if final_bool == 0:
        return False
    return True


def index_unlocked(box: list) -> tuple:
    """ Create a list of indices and a list of boolean values"""
    box_lenght = len(box)
    indecies = list(range(box_lenght))
    unlocked = []
    unlocked.append(True)
    for b in range(box_lenght - 1):
        unlocked.append(False)
    return indecies, unlocked


def get_keys(box: list, index: int, unlocked: list, keys: list) -> list:
    """ Returns available keys"""
    if unlocked[index] is False:
        return keys
    for b in box:
        keys.append(b)
    return keys


def run(boxes: list,
        keys: list,
        unlocked: list,
        lenght: int,
        used: list
        ) -> list:
    """
    Recursive function to use keys on all boxes
        Args:
            boxes: list of boxes
            keys: list of keys
            unlocked: boolean list
            lenght: lenght of boxes
            used: list of all used keys
        Returns: unlocked (final state)
    """
    if lenght <= 0:
        return unlocked
    new_keys_set = set()

    for key in keys:
        unlocked[key] = True
        new_keys_set = new_keys_set.union(boxes[key])
        used.append(key)
    new_keys_list = list(new_keys_set)

    for key in new_keys_list:
        if key in used:
            new_keys_list.remove(key)
    return run(boxes, new_keys_list, unlocked, lenght - 1, used)


def canUnlockAll(boxes: list) -> bool:
    """ Checks if boxes can be unlocked.
        Args: Boxes: A list of boxes to check
        Returns: True if all boxes can be opened, else return False
    """
    box_lenght = len(boxes)
    _, unlocked = index_unlocked(boxes)
    key_pool = [keys for keys in boxes[0]]
    used_keys = []
    bool_list = run(boxes, key_pool, unlocked, box_lenght, used_keys)
    return evaluate_truthy(bool_list)
