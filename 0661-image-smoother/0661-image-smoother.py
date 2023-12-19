from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                result[i][j] = self.smoothCell(img, i, j, m, n)

        return result

    def smoothCell(self, img, i, j, m, n):
        total, count = 0, 0

        for x in range(max(0, i-1), min(m, i+2)):
            for y in range(max(0, j-1), min(n, j+2)):
                total += img[x][y]
                count += 1

        return total // count