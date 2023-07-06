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

    for i in range(num_boxes):
        if unlocked[i]:
            for key in boxes[i]:
                if key < num_boxes and not unlocked[key]:
                    unlocked[key] = True

    return all(unlocked)
