"""
438. 找到字符串中所有字母异位词
难度：中等
链接：https://leetcode.cn/problems/find-all-anagrams-in-a-string/

给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

示例 1:

    输入: s = "cbaebabacd", p = "abc"
    输出: [0,6]
    解释:
    起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
    起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

 示例 2:

    输入: s = "abab", p = "ab"
    输出: [0,1,2]
    解释:
    起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
    起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
    起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

提示:

- 1 <= s.length, p.length <= 3 * 10⁴

- s 和 p 仅包含小写字母
"""

class Solution:

    def findAnagrams(self, s: str, p: str) -> list[int]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 : s = "cbaebabacd", p = "abc"
    # 期望输出：: [0,6]
    print(s.findAnagrams("cbaebabacd", "abc"))

    # 示例 2：输入 : s = "abab", p = "ab"
    # 期望输出：: [0,1,2]
    print(s.findAnagrams("abab", "ab"))
