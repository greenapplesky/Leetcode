class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createList(str):
    res = ListNode(-1)
    ptr = res
    for element in str:
        node = ListNode(int(element))
        ptr.next = node
        ptr = ptr.next
    return res.next