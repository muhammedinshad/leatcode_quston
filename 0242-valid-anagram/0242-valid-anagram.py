class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        res = False
        if len(t) == len(s):
            for i in s:
                if s.count(i) == t.count(i):
                    res=True
                else:
                    res = False
                    break
        return res

                
        