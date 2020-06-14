#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        reach, end, count = 0, 0, 0
        for i in range(len(nums) - 1):
            if i <= reach:
                reach = max(reach, nums[i] + i)
                if i == end:
                    end =reach
                    count += 1

        return count