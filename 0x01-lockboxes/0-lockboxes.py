#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Check if all the boxes can be opened.

    Args:
        boxes (list): List of lists representing the boxes and their corresponding keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # Number of boxes
    visited = [False] * n  # Keep track of visited boxes
    visited[0] = True  # Mark the first box as visited
    queue = [0]  # Start the queue with the first box

    while queue:
        box = queue.pop(0)  # Get the next box from the queue
        keys = boxes[box]  # Get the keys inside the current box

        for key in keys:
            if 0 <= key < n and not visited[key]:
                visited[key] = True  # Mark the box as visited
                queue.append(key)  # Add the box to the queue

    return all(visited)


if __name__ == '__main__':
    boxes = [[1], [2], [3], [4], []]
    print(can_unlock_all(boxes))  # Output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(can_unlock_all(boxes))  # Output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(can_unlock_all(boxes))  # Output: False
