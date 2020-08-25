# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        res = ListNode(0)
        ptr = res
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum//10
            ptr.next = ListNode(sum % 10)
            ptr = ptr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry == 1:
            ptr.next = ListNode(1)
        return res.next

solution = Solution()
l10 = ListNode(2)
l11 = ListNode(4)
l12 = ListNode(3)
l20 = ListNode(5)
l21 = ListNode(6)
l22 = ListNode(4)
l10.next = l11
l11.next = l12
l20.next = l21
l21.next = l22
res = solution.addTwoNumbers(l10,l20)
ptr = res
while ptr:
    print(ptr.val)
    ptr = ptr.next
