# 143. 重排链表
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ListNode import ListNode,createList


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        ReverseHead = self.__reverse(slow.next)
        slow.next = None
        ptr1 = head
        ptr2 = ReverseHead
        while ptr1 and ptr2:
            tmp1 = ptr1.next
            tmp2 = ptr2.next
            ptr1.next = ptr2
            ptr2.next = tmp1
            ptr1 = tmp1
            ptr2 = tmp2

    def __reverse(self,head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        ptr = head
        while ptr and ptr.next:
            tmp = ptr.next
            ptr.next = tmp.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next


str = "12345"
head = createList(str)
sol = Solution()
sol.reorderList(head)
print("123")