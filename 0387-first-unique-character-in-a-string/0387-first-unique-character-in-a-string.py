class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        frq = {}
        for i in s:
            frq[i] = frq.get(i,0) +1

        for j in range(len(s)):
            if frq[s[j]] == 1:
                return j
        return -1    
        