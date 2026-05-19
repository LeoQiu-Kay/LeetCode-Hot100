"""
108. 将有序数组转换为二叉搜索树
难度：简单
链接：https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/

给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

示例 1：

    输入：nums = [-10,-3,0,5,9]
    输出：[0,-3,9,-10,null,5]
    解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：

    输入：nums = [1,3]
    输出：[3,1]
    解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。

提示：

- 1 <= nums.length <= 10⁴

- -10⁴ <= nums[i] <= 10⁴

- nums 按 严格递增 顺序排列
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(items):
    """用 LeetCode 层序数组（null 用 None 表示）构造二叉树。"""
    if not items:
        return None
    root = TreeNode(items[0])
    queue = [root]
    i = 1
    while queue and i < len(items):
        node = queue.pop(0)
        # 左孩子
        if i < len(items) and items[i] is not None:
            node.left = TreeNode(items[i])
            queue.append(node.left)
        i += 1
        # 右孩子
        if i < len(items) and items[i] is not None:
            node.right = TreeNode(items[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 nums = [-10,-3,0,5,9]
    # 期望输出：[0,-3,9,-10,null,5]
    print(s.sortedArrayToBST([-10,-3,0,5,9]))

    # 示例 2：输入 nums = [1,3]
    # 期望输出：[3,1]
    print(s.sortedArrayToBST([1,3]))
