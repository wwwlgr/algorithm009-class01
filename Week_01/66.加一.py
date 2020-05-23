#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            if not digits:
                return []
            n = len(digits)
            ret = [0] * n
            carry = 1
            for i in reversed(range(n)):
                s = digits[i] + carry
                ret[i] = s % 10
                carry = s // 10
            
            if carry:
                ret = [1] + ret
            return ret


                