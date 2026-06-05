"""
221. 最大正方形
难度：中等
链接：https://leetcode.cn/problems/maximal-square/

📌 不在 Hot 100 题单，作为二维 DP 的经典母题补充。

在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

示例 1：

    输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    输出：4

示例 2：

    输入：matrix = [["0","1"],["1","0"]]
    输出：1

示例 3：

    输入：matrix = [["0"]]
    输出：0

提示：

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300
- matrix[i][j] 为 '0' 或 '1'
"""


class Solution:

    def maximalSquare(self, matrix: list[list[str]]) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # 期望输出：4
    print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

    # 示例 2：输入 matrix = [["0","1"],["1","0"]]
    # 期望输出：1
    print(s.maximalSquare([["0","1"],["1","0"]]))

    # 示例 3：输入 matrix = [["0"]]
    # 期望输出：0
    print(s.maximalSquare([["0"]]))
