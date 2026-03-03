class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        org = [i.lower() for i in s if i.isalpha() or i.isdigit()]
        rvs = org[::-1]
        return org == rvs