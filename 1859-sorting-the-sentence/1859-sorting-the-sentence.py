class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = [""] * len(words)

        for word in words:
            index = int(word[-1]) - 1
            result[index] = word[:-1]

        return " ".join(result)
        