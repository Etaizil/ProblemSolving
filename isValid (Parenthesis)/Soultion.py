def isValid(s: str) -> bool:  # Using dictionary to shorten code
    stack = []
    bracketsMap = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in bracketsMap.values():
            stack.append(char)
        elif char in bracketsMap:
            if (not stack) or (stack.pop() != bracketsMap[char]):
                return False
        else:
            return False
    return not stack


"""
# Naive solution, using conditions for every parenthesis
def isValid(s: str) -> bool:  # Using dictionary to shorten code
    stack = []
    for p in s:
        if p == "(" or p == "{" or p == "[":
            stack.append(p)
            continue
        if stack:
            if p == ")":
                if stack[-1] == "(":
                    stack.pop()
                    continue
                else:
                    return False
            elif p == "}":
                if stack[-1] == "{":
                    stack.pop()
                    continue
                else:
                    return False
            elif p == "]":
                if stack[-1] == "[":
                    stack.pop()
                    continue
                else:
                    return False
        else:
            return False
    if stack:
        return False
    return True
"""
