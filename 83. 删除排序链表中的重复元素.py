# 83. 删除排序链表中的重复元素
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = ListNode(0)
        res.next = head
        ptr1 = res
        while ptr1:
            ptr2 = ptr1.next
            while ptr2 and ptr2.next and ptr2.val == ptr2.next.val:
                ptr2 = ptr2.next
            if ptr2:
                ptr1.next = ptr2
            ptr1 = ptr1.next
        return res.next

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        ptr1 = head
        while ptr1 and ptr1.next:
            if ptr1.val == ptr1.next.val:
                ptr1.next = ptr1.next.next
            else:
                ptr1 = ptr1.next
        return head


sol = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(3)
l5 = ListNode(4)
l6 = ListNode(4)
l7 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
res = sol.deleteDuplicates2(l1)
print("123")