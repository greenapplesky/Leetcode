# 160. 相交链表
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from ListNode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha, hb = headA, headB
        while ha != hb:
            if ha is None:
                ha = headB
            else:
                ha = ha.next
            if hb is None:
                hb = headA
            else:
                hb = hb.next
        return ha
