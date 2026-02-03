class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = sorted(list(map(lambda x: x*x ,nums)))
        return res     