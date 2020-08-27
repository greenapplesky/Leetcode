# 92. 反转链表 II
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ListNode import ListNode, createList


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        ptr = res = ListNode(0)
        res.next = head
        while m > 0:
            curhead = ptr
            ptr = ptr.next
            m = m - 1
            n = n - 1
        while n > 0:
            tmp = ptr.next
            ptr.next = ptr.next.next
            tmp.next = curhead.next
            curhead.next = tmp
            n = n - 1
        return res.next


str = "12345"
head = createList(str)
sol = Solution()
res = sol.reverseBetween(head, 2, 4)
print("123")