class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        ms = 0
        ns = 0
        for i in range(1,n+1):
            if i%m == 0:
                ms +=i
            else :
                ns +=i    
        return ns - ms