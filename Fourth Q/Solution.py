def decode(word: str) -> str:
    if not word:
        return ""
    retStr = ""
    count = 0
    while count < len(word):
        if word[count].isdigit():
            repetitions = ""
            while count < len(word) and word[count].isdigit():
                repetitions += word[count]
                count += 1
            if count < len(word):
                character = word[count]
            else:
                break
        else:
            character = word[count]
            repetitions = "1"
        retStr += character * int(repetitions)
        count += 1
    return retStr
