class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        alice = [i for i in nums if i < 10]
        bob = [i for i in nums if i >= 10]
       
        return sum(alice) != sum(bob)