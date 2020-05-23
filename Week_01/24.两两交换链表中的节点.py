#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        # while pre.next and pre.next.next:
        #     a = pre.next
        #     b = a.next
        #     pre.next, b.next, a.next = b, a, b.next
        #     pre = a
        # return self.next
        while head and head.next:
            a = head
            b = head.next
            pre.next , b.next , a.next = b, a, b.next
            pre = a
            head = a.next
        return self.next