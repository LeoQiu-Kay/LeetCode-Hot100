"""
230. 二叉搜索树中第 K 小的元素
难度：中等
链接：https://leetcode.cn/problems/kth-smallest-element-in-a-bst/

给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（k 从 1 开始计数）。

示例 1：

    输入：root = [3,1,4,null,2], k = 1
    输出：1

示例 2：

    输入：root = [5,3,6,2,4,null,null,1], k = 3
    输出：3

提示：

- 树中的节点数为 n 。

- 1 <= k <= n <= 10⁴

- 0 <= Node.val <= 10⁴

进阶： 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
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

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [3,1,4,null,2], k = 1
    # 期望输出：1
    print(s.kthSmallest(list_to_tree([3,1,4,None,2]), 1))

    # 示例 2：输入 root = [5,3,6,2,4,null,null,1], k = 3
    # 期望输出：3
    print(s.kthSmallest(list_to_tree([5,3,6,2,4,None,None,1]), 3))
