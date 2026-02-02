class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        c= 0
        value = ""
        for i in sentences:
            b = i.split(" ")
            if len(b) > c:
                c = len(b)
                value  = i

        return c