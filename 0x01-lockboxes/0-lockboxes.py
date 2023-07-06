#!/usr/bin/python3
"""
Module: 0-lockboxes
Contains a method `canUnlockAll` that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Method: canUnlockAll
    Determines if all the boxes can be opened.
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True
    keys = [0]

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
