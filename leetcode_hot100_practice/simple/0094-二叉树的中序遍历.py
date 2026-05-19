"""
94. 二叉树的中序遍历
难度：简单
链接：https://leetcode.cn/problems/binary-tree-inorder-traversal/

给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

示例 1：

    输入：root = [1,null,2,3]
    输出：[1,3,2]

示例 2：

    输入：root = []
    输出：[]

示例 3：

    输入：root = [1]
    输出：[1]

提示：

- 树中节点数目在范围 [0, 100] 内

- -100 <= Node.val <= 100

进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [1,null,2,3]
    # 期望输出：[1,3,2]
    print(s.inorderTraversal(list_to_tree([1,None,2,3])))

    # 示例 2：输入 root = []
    # 期望输出：[]
    print(s.inorderTraversal(list_to_tree([])))

    # 示例 3：输入 root = [1]
    # 期望输出：[1]
    print(s.inorderTraversal(list_to_tree([1])))
