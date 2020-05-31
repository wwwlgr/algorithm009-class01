#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        return self.dfs(n, 0, 0, 0, 0)
    
    def dfs(self, n, row, v1, v2, v3):
        if row == n:
            return 1

        count = 0
        for col in range(n):
            if self.isValid(col, v1, v2, v3):
                s = 1 << col
                count += self.dfs(n, row + 1, v1 | s, (v2 | s) >> 1, (v3 | s ) << 1)
        return count
    
    def isValid(self, col, v1, v2, v3):
        s = 1 << col
        if v1 & s or v2 & s or v3 & s:
            return False
        return True


# @lc code=end

