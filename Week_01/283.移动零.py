#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums) - 1:
            if nums[left] == 0:
                nums[left:-1] = nums[left+1:]
                right += 1
                nums[-1] = 0
            else:
                left += 1
                right += 1

        


# @lc code=end

