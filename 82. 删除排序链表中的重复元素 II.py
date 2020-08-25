# 82. 删除排序链表中的重复元素 II
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3

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
            flag = 0
            while ptr2:
                if ptr2.next and ptr2.val == ptr2.next.val:
                    flag = 1
                    ptr2 = ptr2.next
                else:
                     break
            if flag == 1:
                ptr1.next = ptr2.next
            else:
                ptr1 = ptr1.next
        return res.next


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
res = sol.deleteDuplicates(l1)
print("123")