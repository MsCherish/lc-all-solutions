class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []  #定义一个栈结构
        d = ["()", "[]", "{}"]
        for i in range(0, len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and stack[-2]+stack[-1] in d:  #匹配就直接出栈
                stack.pop()  
                stack.pop()
        return len(stack) == 0   
        
