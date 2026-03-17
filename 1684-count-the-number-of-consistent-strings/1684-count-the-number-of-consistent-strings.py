class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            is_active = True
            for char in word:
                if char not in allowed:
                    is_active = False
                    break
            if is_active:                  
                count += 1
        return count       