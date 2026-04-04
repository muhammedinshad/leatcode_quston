class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        ary =[]
        for i in nums:
            count =0
            for j in nums:
                if j < i:
                    count += 1
            ary.append(count)
        return ary
        