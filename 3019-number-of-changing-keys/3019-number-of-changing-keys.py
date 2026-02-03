class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        c =''
        count = 0
        for i in s:
            if i.lower() != c.lower():
                c=i
                count += 1
        return count - 1  