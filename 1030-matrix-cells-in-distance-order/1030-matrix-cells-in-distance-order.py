class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        cells = []

        for r in range(rows):
            for c in range(cols):
                cells.append([r, c])

        # Sort by Manhattan distance
        cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))

        return cells