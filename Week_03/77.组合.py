#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(n, k-1, -1) for pre in self.combine(i-1, k-1)]

        