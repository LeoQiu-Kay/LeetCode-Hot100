"""
226. 翻转二叉树
难度：简单
链接：https://leetcode.cn/problems/invert-binary-tree/

给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

示例 1：

    输入：root = [4,2,7,1,3,6,9]
    输出：[4,7,2,9,6,3,1]

示例 2：

    输入：root = [2,1,3]
    输出：[2,3,1]

示例 3：

    输入：root = []
    输出：[]

提示：

- 树中节点数目范围在 [0, 100] 内

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

    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [4,2,7,1,3,6,9]
    # 期望输出：[4,7,2,9,6,3,1]
    print(s.invertTree(list_to_tree([4,2,7,1,3,6,9])))

    # 示例 2：输入 root = [2,1,3]
    # 期望输出：[2,3,1]
    print(s.invertTree(list_to_tree([2,1,3])))

    # 示例 3：输入 root = []
    # 期望输出：[]
    print(s.invertTree(list_to_tree([])))
