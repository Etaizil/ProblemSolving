from Solution import *

list1 = [1, 2]
list2 = [3, 4]
median1 = 2.5

list3 = [1, 2]
list4 = [3]
median2 = 2

res1 = findMedianSortedArrays(list1, list2)
if res1 != 2.5:
    print("Wrong in res1")
else:
    print("Correct in res1")

res2 = findMedianSortedArrays(list3, list4)
if res2 != 2:
    print("Wrong in res2")
else:
    print("Correct in res2")
