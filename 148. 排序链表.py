# 148. 排序链表
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2:
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ListNode import ListNode,createList


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(dummy.next)
        ptr = dummy
        while left and right:
            if left.val < right.val:
                ptr.next = left
                left = left.next
            else:
                ptr.next = right
                right = right.next
            ptr = ptr.next
        if left is None: ptr.next = right
        if right is None: ptr.next = left
        return dummy.next


str = ""
head = createList(str)
sol = Solution()
res = sol.sortList(head)
print("123")
