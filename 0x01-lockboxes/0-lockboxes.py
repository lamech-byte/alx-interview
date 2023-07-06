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
    keys = boxes[0]

    for key in keys:
        if key < num_boxes:
            unlocked[key] = True
            keys += boxes[key]

    return all(unlocked)
