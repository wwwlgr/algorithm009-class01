#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = self
        pre = hair
        hair.next = head
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next

            nex = tail.next
            head , tail = self.reverse(head , tail)
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next

    def reverse(self, head, tail):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail , head

            
        
# @lc code=end

