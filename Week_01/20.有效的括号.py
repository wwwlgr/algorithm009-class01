#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0: return False
        dic = {"(" : ")" ,  "[": "]", "{" : "}"}
        stack = []
        for i in range(len(s)):
            if len(stack) == 0 :
                if s[i] in dic.keys():
                    stack.append(s[i])
                else :
                    return False
            else :
                if s[i] in dic.keys():
                    stack.append(s[i])
                else:
                    if s[i] == dic[stack[-1]]:
                        stack.pop()
                    else: 
                        return False

        if len(stack) == 0:
            return True
        else:
            return False



# @lc code=end


