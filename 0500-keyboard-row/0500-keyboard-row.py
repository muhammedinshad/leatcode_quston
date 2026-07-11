class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        ans = []
        for word in words:
            w = word.lower()
            for row in rows:
                if all(ch in row for ch in w):
                    ans.append(word)
                    break

        return ans
        