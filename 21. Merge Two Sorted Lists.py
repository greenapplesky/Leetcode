# 21.合并两个有序链表
# 将两个升序链表合并为一个新的
# 升序
# 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        ptr = res
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        if l1:
            ptr.next = l1
        else:
            ptr.next = l2
        return res.next


sol = Solution()
l10 = ListNode(1)
l11 = ListNode(2)
l12 = ListNode(4)
l20 = ListNode(1)
l21 = ListNode(3)
l22 = ListNode(4)
l10.next = l11
l11.next = l12
l20.next = l21
l21.next = l22
res = sol.mergeTwoLists(l10, l20)
print("123")