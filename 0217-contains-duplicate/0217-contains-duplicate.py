class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        value = set()
        for i in nums:
            if i in value:
                return True
            value.add(i)
        return False            