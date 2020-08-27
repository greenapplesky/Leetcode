# 86. 分隔链表
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode, createList


class Solution:
    # 记录cut节点为分隔线，搞不定。。。
    # def partition(self, head: ListNode, x: int) -> ListNode:
    #     res = ListNode(0)
    #     res.next = head
    #     ptr = res
    #     cut = res
    #     while ptr.next:
    #         if ptr.next.val >= x:
    #             ptr = ptr.next
    #         else:
    #             tmp1 = cut.next
    #             tmp2 = ptr.next.next
    #             cut.next = ptr.next
    #             cut.next.next = tmp1
    #             ptr.next = tmp2
    #     return res.next

    def partition(self, head: ListNode, x: int) -> ListNode:
        left = left_head = ListNode(0)
        right = right_head = ListNode(0)
        ptr = head
        while ptr:
            if ptr.val < x:
                left.next = ptr
                left = left.next
            else:
                right.next = ptr
                right = right.next
            ptr = ptr.next
        left.next = right_head.next
        right.next = None
        return left_head.next


x = 3
str = "143252"
head = createList(str)
sol = Solution()
res = sol.partition(head,x)
print("123")