"""
104. 二叉树的最大深度
难度：简单
链接：https://leetcode.cn/problems/maximum-depth-of-binary-tree/

给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

示例 1：

    输入：root = [3,9,20,null,null,15,7]
    输出：3

示例 2：

    输入：root = [1,null,2]
    输出：2

提示：

- 树中节点的数量在 [0, 10⁴] 区间内。

- -100 <= Node.val <= 100
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

    def maxDepth(self, root: TreeNode | None) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [3,9,20,null,null,15,7]
    # 期望输出：3
    print(s.maxDepth(list_to_tree([3,9,20,None,None,15,7])))

    # 示例 2：输入 root = [1,null,2]
    # 期望输出：2
    print(s.maxDepth(list_to_tree([1,None,2])))
