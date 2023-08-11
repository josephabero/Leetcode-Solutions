"""
Min Stack
https://leetcode.com/problems/min-stack
"""

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimums = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

        minimum = val
        if self.minimums:
            # Compare value to the last minimum value
            minimum = val if val < self.minimums[-1] else self.minimums[-1]
        self.minimums.append(minimum)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0:
            val = self.stack.pop()
            self.minimums.pop()
        return None


    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        return None


    def getMin(self):
        """
        :rtype: int
        """
        return self.minimums[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
