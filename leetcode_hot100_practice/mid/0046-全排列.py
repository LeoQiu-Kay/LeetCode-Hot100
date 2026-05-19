"""
46. 全排列
难度：中等
链接：https://leetcode.cn/problems/permutations/

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：

    输入：nums = [1,2,3]
    输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：

    输入：nums = [0,1]
    输出：[[0,1],[1,0]]

示例 3：

    输入：nums = [1]
    输出：[[1]]

提示：

- 1 <= nums.length <= 6

- -10 <= nums[i] <= 10

- nums 中的所有整数 互不相同
"""

class Solution:

    def permute(self, nums: list[int]) -> list[list[int]]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 nums = [1,2,3]
    # 期望输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(s.permute([1,2,3]))

    # 示例 2：输入 nums = [0,1]
    # 期望输出：[[0,1],[1,0]]
    print(s.permute([0,1]))

    # 示例 3：输入 nums = [1]
    # 期望输出：[[1]]
    print(s.permute([1]))
