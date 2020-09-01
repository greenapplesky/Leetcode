# 142.环形链表II
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回null。
#
# 为了表示给定链表中的环，我们使用整数pos来表示链表尾连接到链表中的位置（索引从0开始）。 如果pos是 - 1，则在该链表中没有环。
#
# 说明：不允许修改给定的链表。
#
# 示例
# 1：
#
# 输入：head = [3, 2, 0, -4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
# 示例
# 2：
#
# 输入：head = [1, 2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
# 示例
# 3：
#
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ListNode import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None: return None
        slow = fast = head
        while True:
            if not (fast and fast.next): return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
