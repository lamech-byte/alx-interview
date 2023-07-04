#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)  # Number of boxes
    visited = [False] * n  # Keep track of visited boxes
    visited[0] = True  # Mark the first box as visited
    queue = [0]  # Start the queue with the first box

    while queue:
        box = queue.pop(0)  # Get the next box from the queue
        keys = boxes[box]  # Get the keys inside the current box

        for key in keys:
            if key < n and not visited[key]:
                visited[key] = True  # Mark the box as visited
                queue.append(key)  # Add the box to the queue

    return all(visited)
