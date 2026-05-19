"""
105. 从前序与中序遍历序列构造二叉树
难度：中等
链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1:

    输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    输出: [3,9,20,null,null,15,7]

示例 2:

    输入: preorder = [-1], inorder = [-1]
    输出: [-1]

提示:

- 1 <= preorder.length <= 3000

- inorder.length == preorder.length

- -3000 <= preorder[i], inorder[i] <= 3000

- preorder 和 inorder 均 无重复 元素

- inorder 均出现在 preorder

- preorder 保证 为二叉树的前序遍历序列

- inorder 保证 为二叉树的中序遍历序列
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

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 : preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    # 期望输出：: [3,9,20,null,null,15,7]
    print(s.buildTree([3,9,20,15,7], [9,3,15,20,7]))

    # 示例 2：输入 : preorder = [-1], inorder = [-1]
    # 期望输出：: [-1]
    print(s.buildTree([-1], [-1]))
