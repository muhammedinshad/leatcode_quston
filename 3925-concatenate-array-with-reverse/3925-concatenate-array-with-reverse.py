class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        
        for i in range(n-1,-1,-1):
            res.append(nums[i])
        return nums + res
        