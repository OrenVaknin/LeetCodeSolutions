class Solution(object):
    def shortestWord(self, strs):
        shortest= strs[0]
        for s in strs:
            if len(s)<len(shortest):
                shortest=s
        return shortest
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest= self.shortestWord(strs)
        for i in range(len(shortest)):  
            char=strs[0][i]
            for j in strs:
                if j[i]!=char:
                    return j[:i]
        return shortest
