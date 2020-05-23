#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        try:
            self.stack.pop()
        except Exception as e:
            pass
        

    def top(self) -> int:
        try :
            x = self.stack[-1]
        except Exception as e:
            return None
        else:
            return x

    def getMin(self) -> int:
        try:
            mi = min(self.stack)
        except Exception as e:
            return None
        else: 
            return mi



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

