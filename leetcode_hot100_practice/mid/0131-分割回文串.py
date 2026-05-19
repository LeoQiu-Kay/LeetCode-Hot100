"""
131. 分割回文串
难度：中等
链接：https://leetcode.cn/problems/palindrome-partitioning/

给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

示例 1：

    输入：s = "aab"
    输出：[["a","a","b"],["aa","b"]]

示例 2：

    输入：s = "a"
    输出：[["a"]]

提示：

- 1 <= s.length <= 16

- s 仅由小写英文字母组成
"""

class Solution:

    def partition(self, s: str) -> list[list[str]]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 s = "aab"
    # 期望输出：[["a","a","b"],["aa","b"]]
    print(s.partition("aab"))

    # 示例 2：输入 s = "a"
    # 期望输出：[["a"]]
    print(s.partition("a"))
