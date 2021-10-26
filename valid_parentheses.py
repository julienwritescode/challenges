# Source: https://leetcode.com/problems/valid-parentheses/
# Author: Julien
# Execution time: O(n)
# Help needed: No

def isValid(s: str) -> bool:
    # If uneven, return False
    if len(s) % 2 != 0:
        return False

    a = {'(': 1, '[': 2, '{': 3, '}': 4, ']': 5, ')': 6}
    stack = []

    for p in s:
        if a[p] < 4:
            stack.append(p)
        elif len(stack) > 0:
            if a[p] + a[stack[-1]] != 7:
                return False
            else:
                stack.pop()
        else:
            return False

    return True if len(stack) == 0 else False
