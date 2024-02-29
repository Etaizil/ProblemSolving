from Solution import *

strTest1 = "aabcc"
strTest2 = ""
strTest3 = "aabca"
strTest4 = "aAbb"

res1 = encode(strTest1)
res2 = encode(strTest2)
res3 = encode(strTest3)
res4 = encode(strTest4)

print("Correct in test1") if res1 == "2a1b2c" else print("Wrong in test1")
print("Correct in test2") if res2 == "" else print("Wrong in test2")
print("Correct in test3") if res3 == "2a1b1c1a" else print("Wrong in test3")
print("Correct in test4") if res4 == "1a1A2b" else print("Wrong in test4")
