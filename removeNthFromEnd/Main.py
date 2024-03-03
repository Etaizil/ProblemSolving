from Solution import *

valuesArr1 = [1, 2, 3, 4, 5]
head1 = createLinkedList(valuesArr1)
n1 = 2

valuesArr2 = [1, 2, 3, 4, 5, 6, 7, 8]
head2 = createLinkedList(valuesArr2)
n2 = 1

valuesArr3 = [1, 2]
head3 = createLinkedList(valuesArr3)
n3 = 1

valuesArr4 = [1]
head4 = createLinkedList(valuesArr4)
n4 = 1

valuesArr5 = [1, 2]
head5 = createLinkedList(valuesArr5)
n5 = 3

res1 = removeNthFromEnd(head1, n1)
res2 = removeNthFromEnd(head2, n2)
res3 = removeNthFromEnd(head3, n3)
res4 = removeNthFromEnd(head4, n4)
res5 = removeNthFromEnd(head5, n5)

expectedResults = [
    ([1, 2, 3, 5], res1),
    ([1, 2, 3, 4, 5, 6, 7], res2),
    ([1], res3),
    ([], res4),
    ([1, 2], res5),
]

for i, (expected, result) in enumerate(expectedResults, start=1):
    resultValues = LinkedListToValues(result)
    if resultValues != expected:
        print(f"Wrong in res{i}: {resultValues}")
    else:
        print(f"Correct in res{i}")
