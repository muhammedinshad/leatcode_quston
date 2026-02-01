class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = max(nums)
        for i in range(n+1):
            if i not in nums:
                return i
                break     
        if n+1 not in nums:
            return n+1