class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)

        diff = (alice_sum - bob_sum) // 2

        bob_set = set(bobSizes)

        for x in aliceSizes:
            if x - diff in bob_set:
                return [x, x - diff]
        