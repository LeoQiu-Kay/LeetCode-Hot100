"""
543. 二叉树的直径
难度：简单
链接：https://leetcode.cn/problems/diameter-of-binary-tree/

给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。

示例 1：

    输入：root = [1,2,3,4,5]
    输出：3
    解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。

示例 2：

    输入：root = [1,2]
    输出：1

提示：

- 树中节点数目在范围 [1, 10⁴] 内

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

    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [1,2,3,4,5]
    # 期望输出：3
    print(s.diameterOfBinaryTree(list_to_tree([1,2,3,4,5])))

    # 示例 2：输入 root = [1,2]
    # 期望输出：1
    print(s.diameterOfBinaryTree(list_to_tree([1,2])))
