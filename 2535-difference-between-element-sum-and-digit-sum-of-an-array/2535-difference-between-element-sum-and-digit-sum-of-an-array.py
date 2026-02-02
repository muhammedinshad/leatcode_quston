class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rse =""
        c = 0
        for i in nums:
            rse += str(i)
        for j in rse:
            c += int(j)       
        return sum(nums) - c      