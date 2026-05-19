"""
32. 最长有效括号
难度：困难
链接：https://leetcode.cn/problems/longest-valid-parentheses/

给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。

左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。

示例 1：

    输入：s = "(()"
    输出：2
    解释：最长有效括号子串是 "()"

示例 2：

    输入：s = ")()())"
    输出：4
    解释：最长有效括号子串是 "()()"

示例 3：

    输入：s = ""
    输出：0

提示：

- 0 <= s.length <= 3 * 10⁴

- s[i] 为 '(' 或 ')'
"""

class Solution:

    def longestValidParentheses(self, s: str) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 s = "(()"
    # 期望输出：2
    print(s.longestValidParentheses("(()"))

    # 示例 2：输入 s = ")()())"
    # 期望输出：4
    print(s.longestValidParentheses(")()())"))

    # 示例 3：输入 s = ""
    # 期望输出：0
    print(s.longestValidParentheses(""))
