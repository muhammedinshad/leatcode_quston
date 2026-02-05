class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for i in nums:
            if i == 0:
                return i
            elif i < 0:
                c +=1
        if c%2 == 0:
            return 1
        else :
            return -1