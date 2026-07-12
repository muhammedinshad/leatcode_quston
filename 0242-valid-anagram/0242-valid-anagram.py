class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for c in t:
            idx = ord(c) - ord('a')
            cnt[idx] -= 1
            if cnt[idx] < 0:
                return False

        return True
        