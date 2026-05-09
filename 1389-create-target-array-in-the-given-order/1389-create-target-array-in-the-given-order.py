class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        arr = []
        for n in range(len(nums)):
            arr.insert(index[n],nums[n])
        return arr
        