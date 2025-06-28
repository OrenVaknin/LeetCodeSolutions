class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {')':'(',']':'[','}':'{'}
        for char in s:
            if char in map.values():
                stack.append(char)
            elif char in map:
                if not stack or stack.pop()!=map[char]:
                    return False
            else: return False
        return not stack
        
        """
        rounded=0
        curly=0
        square=0
        for char in s:
            if char=="(":
                rounded+=1
            elif char==")":
                rounded-=1
            elif char=="[":
                square+=1
            elif char=="]":
                square-=1
            elif char=="{":
                curly+=1
            elif char=="}":
                curly-=1
            if square==-1 or curly==-1 or rounded==-1:
                return False
        if square!=0 or curly!=0 or rounded!=0:
            return False
        return True
        """