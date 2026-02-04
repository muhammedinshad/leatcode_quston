class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        a = list(str(n))
        x=1
        for i in range(len(a)):
                x=x*int(a[i])
                c += int(a[i])
        return x-c       