class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not len(s) == len(t):
            for char in t:
                if s.count(char) != t.count(char):
                    return char   