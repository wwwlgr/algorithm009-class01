#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while True:
            if not (fast and fast.next) : return
            fast = fast.next.next
            slow = slow.next
            if fast == slow : break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast

        

