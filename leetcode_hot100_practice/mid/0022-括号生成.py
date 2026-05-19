"""
22. 括号生成
难度：中等
链接：https://leetcode.cn/problems/generate-parentheses/

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：

    输入：n = 3
    输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：

    输入：n = 1
    输出：["()"]

提示：

- 1 <= n <= 8
"""

class Solution:

    def generateParenthesis(self, n: int) -> list[str]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 n = 3
    # 期望输出：["((()))","(()())","(())()","()(())","()()()"]
    print(s.generateParenthesis(3))

    # 示例 2：输入 n = 1
    # 期望输出：["()"]
    print(s.generateParenthesis(1))
