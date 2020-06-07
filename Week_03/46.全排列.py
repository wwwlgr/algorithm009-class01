#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [
            p[:i] + [nums[0]] + p[i:]
            for i in range(len(nums))
            for p in self.permute(nums[1:])
        ] or [[]]


