class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sd = {}
        td = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 in sd:
                if sd[c1] != c2:
                    return False
            else:
                sd[c1] = c2 
            
            if c2 in td:
                if td[c2] != c1:
                    return False
            else :
                td[c2] = c1

        return True            