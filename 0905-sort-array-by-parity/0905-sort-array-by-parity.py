class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        aryy = []
        aryy2 = []
        for i in nums:
            if i%2==0:
                aryy.append(i)
            else:
                aryy2.append(i)
            
        return aryy + aryy2
        