class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # one pointer to the end and count it (start at 1)
    # second pointer = end count - n
    if head is None or (head.next is None and n == 1):
        return None
    length = 0
    copyList = head
    while copyList:  # O(n) to determine length of list
        if n == 0 and not copyList.next:
            return head
        length += 1
        copyList = copyList.next
    if n == length:
        return head.next
    if length < n:
        return head
    secondP = length - n
    counter = 1
    copyList = head
    while counter != secondP:
        counter += 1
        copyList = copyList.next
    if not copyList.next.next:
        copyList.next = None
    else:
        copyList.next = copyList.next.next
    return head


def createLinkedList(values: list):
    head = ListNode()
    current = head
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return head.next


def LinkedListToValues(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values
