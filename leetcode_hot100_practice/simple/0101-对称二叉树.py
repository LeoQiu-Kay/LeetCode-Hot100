"""
101. 对称二叉树
难度：简单
链接：https://leetcode.cn/problems/symmetric-tree/

给你一个二叉树的根节点 root ， 检查它是否轴对称。

示例 1：

    输入：root = [1,2,2,3,4,4,3]
    输出：true

示例 2：

    输入：root = [1,2,2,null,3,null,3]
    输出：false

提示：

- 树中节点数目在范围 [1, 1000] 内

- -100 <= Node.val <= 100

进阶： 你可以运用递归和迭代两种方法解决这个问题吗？
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

    def isSymmetric(self, root: TreeNode | None) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [1,2,2,3,4,4,3]
    # 期望输出：true
    print(s.isSymmetric(list_to_tree([1,2,2,3,4,4,3])))

    # 示例 2：输入 root = [1,2,2,null,3,null,3]
    # 期望输出：false
    print(s.isSymmetric(list_to_tree([1,2,2,None,3,None,3])))
