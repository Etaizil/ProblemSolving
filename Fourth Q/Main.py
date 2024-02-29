from Solution import *

strTest1 = "2a1b2c"
strTest2 = ""
strTest3 = "2a1b1c1a"
strTest4 = "2a1A3b"
strTest5 = "abcd"
strTest6 = "a2b"
strTest7 = "ab3c"


res1 = decode(strTest1)
res2 = decode(strTest2)
res3 = decode(strTest3)
res4 = decode(strTest4)
res5 = decode(strTest5)
res6 = decode(strTest6)
res7 = decode(strTest7)

print("Correct in test1") if res1 == "aabcc" else print(f"Wrong in test1 {res1}")
print("Correct in test2") if res2 == "" else print("Wrong in test2")
print("Correct in test3") if res3 == "aabca" else print(f"Wrong in test3 {res3}")
print("Correct in test4") if res4 == "aaAbbb" else print(f"Wrong in test4 {res4}")
print("Correct in test5") if res5 == "abcd" else print(f"Wrong in test5 {res5}")
print("Correct in test6") if res6 == "abb" else print(f"Wrong in test6 {res6}")
print("Correct in test7") if res7 == "abccc" else print(f"Wrong in test7 {res7}")
