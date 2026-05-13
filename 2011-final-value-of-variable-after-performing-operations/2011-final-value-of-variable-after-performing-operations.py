class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = 0

        for i in operations:
            if i in "X++" or i in "++X":
                res +=1
            else:
                res -= 1
        return res
        