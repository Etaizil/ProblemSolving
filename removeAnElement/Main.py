from Solution import *

nums = [3,2,2,3]
val = 3
result=removeAnElement(nums,val)
if(result!=2):
    print("WRONG in 1")
else:
    print("You are correct in 1")

nums = [0,1,2,2,3,0,4,2]
val = 2
result=removeAnElement(nums,val)
if(result!=5):
    print("WRONG in 2")
else:
    print("You are correct in 2")

nums = [1,1,2,1,1,2,2]
val = 1
result=removeAnElement(nums,val)
if(result!=3):
    print("WRONG in 3")
else:
    print("You are correct in 3")

nums = [1,1,1,1]
val = 1
result=removeAnElement(nums,val)
if(result!=0):
    print("WRONG in 4")
else:
    print("You are correct in 4")

nums = [1,1,1,1]
val = 0
result=removeAnElement(nums,val)
if(result!=4):
    print("WRONG in 5")
else:
    print("You are correct in 5")