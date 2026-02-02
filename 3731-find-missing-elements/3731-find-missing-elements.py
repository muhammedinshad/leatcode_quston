class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arry = []
        for i in range(min(nums),max(nums)+1):
            if i not in nums:
                arry.append(i)
        return arry
           