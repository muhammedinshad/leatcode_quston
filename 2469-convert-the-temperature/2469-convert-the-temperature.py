class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        res = []
        a = celsius + 273.15
        bb = celsius * 1.80 + 32.00
        res.append(a)
        res.append(bb)
        return res
        