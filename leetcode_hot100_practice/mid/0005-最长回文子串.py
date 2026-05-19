"""
5. 最长回文子串
难度：中等
链接：https://leetcode.cn/problems/longest-palindromic-substring/

给你一个字符串 s，找到 s 中最长的 回文 子串。

示例 1：

    输入：s = "babad"
    输出："bab"
    解释："aba" 同样是符合题意的答案。

示例 2：

    输入：s = "cbbd"
    输出："bb"

提示：

- 1 <= s.length <= 1000

- s 仅由数字和英文字母组成
"""

class Solution:

    def longestPalindrome(self, s: str) -> str:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 s = "babad"
    # 期望输出："bab"
    print(s.longestPalindrome("babad"))

    # 示例 2：输入 s = "cbbd"
    # 期望输出："bb"
    print(s.longestPalindrome("cbbd"))
