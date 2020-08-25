# 24.两两交换链表中的节点
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例:
#
# 给定
# 1->2->3->4, 你应该返回
# 2->1->4->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(0)
        res.next = head
        ptr = res
        while ptr.next and ptr.next.next:
            self.swap(ptr)
            ptr = ptr.next.next
        return res.next

    def swap(self, ptr:ListNode):
        l1 = ptr.next
        ptr.next = l1.next
        l1.next = ptr.next.next
        ptr.next.next = l1


sol = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
res = sol.swapPairs(l1)
print("123")