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
        flag = 0
        while(l1 and l2):
            sum = l1.val + l2.val + flag
            flag = sum//10
            ptr.next = ListNode(sum % 10)
            l1 = l1.next
            l2 = l2.next
            ptr = ptr.next
        while(l1):
            sum = l1.val + flag
            flag = sum//10
            ptr.next = ListNode(sum % 10)
            l1 = l1.next
            ptr = ptr.next
        while(l2):
            sum = l2.val + flag
            flag = sum//10
            ptr.next = ListNode(sum % 10)
            l2 = l2.next
            ptr = ptr.next
        if(flag==1):
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
print('111')