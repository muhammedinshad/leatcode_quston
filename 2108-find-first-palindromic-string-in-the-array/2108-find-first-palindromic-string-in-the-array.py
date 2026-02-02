class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        arry = []
        for i in words:
            if i == i[::-1]:
                arry.append(i)
        if len(arry) == 0:
            return ""
        return arry[0] 
        