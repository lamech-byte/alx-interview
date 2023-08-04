#!/usr/bin/python3

import subprocess

def run_command(command):
    try:
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = result.communicate()
        return stdout.strip(), result.returncode
    except FileNotFoundError:
        return "", 1

def test_case(test_input, expected_output):
    command = ["./0-nqueens.py", test_input]
    output, returncode = run_command(command)
    
    print(f"Input: {test_input}")
    print(f"Expected Output:")
    print(expected_output)
    print(f"Output:")
    print(output)
    
    if returncode == 0 and output.strip() == expected_output.strip():
        print("Test Passed!")
        return True
    else:
        print("Test Failed!")
        return False

if __name__ == "__main__":
    test_cases = [
        ("4", "[[0, 1], [1, 3], [2, 0], [3, 2]]\n[[0, 2], [1, 0], [2, 3], [3, 1]]"),
        ("6", "[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]\n[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]\n[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]\n[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]"),
        # Add more test cases if needed
    ]

    total_tests = len(test_cases)
    passed_tests = 0

    for test_input, expected_output in test_cases:
        if test_case(test_input, expected_output):
            passed_tests += 1

    print(f"\nTotal Tests: {total_tests}")
    print(f"Passed Tests: {passed_tests}")
    print(f"Failed Tests: {total_tests - passed_tests}")
