# Problem statement: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
# determine if the input string is valid.
# Solution: O(n), iterate over the string and at each index check if it's opening parentheses or closing parenteses
# If opening the add in stack
# Else check if it's complimentary parentheses is present on top of stack.


def isValid(self, s: str) -> bool:
    stack = []
    dic = {"(": ")", "{": "}", "[": "]"}
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            stack.append(s[i])
        else:
            if len(stack) != 0:
                if dic[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
            else:
                return False
    if len(stack) == 0:
        return True
    return False
