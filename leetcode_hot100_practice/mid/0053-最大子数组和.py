"""
53. 最大子数组和
难度：中等
链接：https://leetcode.cn/problems/maximum-subarray/

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。

示例 1：

    输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出：6
    解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：

    输入：nums = [1]
    输出：1

示例 3：

    输入：nums = [5,4,-1,7,8]
    输出：23

提示：

- 1 <= nums.length <= 10⁵

- -10⁴ <= nums[i] <= 10⁴

进阶： 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
"""

class Solution:

    def maxSubArray(self, nums: list[int]) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 nums = [-2,1,-3,4,-1,2,1,-5,4]
    # 期望输出：6
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

    # 示例 2：输入 nums = [1]
    # 期望输出：1
    print(s.maxSubArray([1]))

    # 示例 3：输入 nums = [5,4,-1,7,8]
    # 期望输出：23
    print(s.maxSubArray([5,4,-1,7,8]))
