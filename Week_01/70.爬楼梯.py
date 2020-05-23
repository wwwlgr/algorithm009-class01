#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a = [1,1,2]
        i = n
        while i > 2:
            a.append(a[-1]+a[-2])
            i -= 1

        return a[n]
# @lc code=end
