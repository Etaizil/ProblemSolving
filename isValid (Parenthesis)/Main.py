from Soultion import *

# 1 True
if isValid("()"):
    print("You are correct in 1")
else:
    print("WRONG in 1")
# 2 False
if isValid("(") == False:
    print("You are correct in 2")
else:
    print("WRONG in 2")
# 3 False
if isValid(")") == False:
    print("You are correct in 3")
else:
    print("WRONG in 3")
# 4 True
if isValid("({[]})") == True:
    print("You are correct in 4")
else:
    print("WRONG in 4")
# 5 False
if isValid("({)}") == False:
    print("You are correct in 5")
else:
    print("WRONG in 5")
# 6 False
if isValid("({}") == False:
    print("You are correct in 6")
else:
    print("WRONG in 6")
# 7 True
if isValid("(){}[]") == True:
    print("You are correct in 7")
else:
    print("WRONG in 7")
