class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_s = s.split(" ")
        for i in reversed(new_s):
            if len(i) !=0:
                return len(i)
                break
        
 
        