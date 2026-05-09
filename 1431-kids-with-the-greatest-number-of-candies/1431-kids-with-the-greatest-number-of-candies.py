class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        bigCandi = max(candies)
        arry = []
        for candi in candies:
            c =candi + extraCandies
            if bigCandi > c:
                arry.append(False)
            
            else:
                arry.append(True)
        return arry
        