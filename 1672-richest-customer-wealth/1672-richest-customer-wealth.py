class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        value = 0
        c = 0
        for i in accounts:
            for j in i:
                c += j
                if c > value:
                    value = c
            c = 0
        return value      