class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {}

        for i, restaurant in enumerate(list1):
            index_map[restaurant] = i

        min_sum = float("inf")
        result = []

        for j, restaurant in enumerate(list2):
            if restaurant in index_map:
                total = index_map[restaurant] + j

                if total < min_sum:
                    min_sum = total
                    result = [restaurant]

                elif total == min_sum:
                    result.append(restaurant)

        return result
        