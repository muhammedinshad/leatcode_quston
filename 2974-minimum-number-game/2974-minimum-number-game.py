class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arry = []
        nums.sort()
        for i in range(0,len(nums),2):
            a = nums[i]
            b = nums[i+1]
            arry.append(b)
            arry.append(a)
        return arry
              
        