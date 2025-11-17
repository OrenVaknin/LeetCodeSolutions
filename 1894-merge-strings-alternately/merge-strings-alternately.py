class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        count1, count2=0,0
        ans=""
        i=0
        while count1 < len(word1) or count2 < len(word2):
            if len(word1)>count1 and len(word2)>count2:
                if i==0:
                    ans+=word1[count1]
                    i=1
                    count1+=1
                elif i==1:
                    ans+=word2[count2]
                    i=0
                    count2+=1
            elif len(word1)>count1:
                ans+=word1[count1]
                count1+=1
            else:
                ans+=word2[count2]
                count2+=1
        return ans


        
