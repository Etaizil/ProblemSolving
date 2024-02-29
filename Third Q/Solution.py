def encode(word: str) -> str:
    if not word:
        return ""
    retStr = ""
    prevChar = 0
    count = 0
    for letter in word:
        if letter == prevChar:
            count += 1
        else:
            if prevChar == 0:
                count += 1
                prevChar = letter
                continue
            retStr += str(count) + prevChar
            prevChar = letter
            count = 1
    retStr += str(count) + prevChar
    return retStr
