# 147.对链表进行插入排序
#
# 插入排序算法：
#
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#
#
# 示例
# 1：
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例
# 2：
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
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        tail = head
        while tail.next:
            ptr = dummy
            while tail.next.val > ptr.next.val:
                ptr = ptr.next
            tail.next = tail.next.next
            tmp = ptr.next
            ptr.next = tail.next
            ptr.next.next = tmp
            tail = tail.next
        return dummy.next


str = "4213"
head = createList(str)
sol = Solution()
res = sol.insertionSortList(head)
print("123")