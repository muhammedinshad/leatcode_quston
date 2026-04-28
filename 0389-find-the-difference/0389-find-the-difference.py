class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
      
        count = 0 
        if not len(s) == len(t):
            for char in t:
                if s.count(char) != t.count(char):
                    return char
        for i in t:
            if i not in s:
                return i         