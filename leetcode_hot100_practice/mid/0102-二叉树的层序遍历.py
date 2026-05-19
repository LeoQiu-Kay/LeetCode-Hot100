"""
102. 二叉树的层序遍历
难度：中等
链接：https://leetcode.cn/problems/binary-tree-level-order-traversal/

给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

示例 1：

    输入：root = [3,9,20,null,null,15,7]
    输出：[[3],[9,20],[15,7]]

示例 2：

    输入：root = [1]
    输出：[[1]]

示例 3：

    输入：root = []
    输出：[]

提示：

- 树中节点数目在范围 [0, 2000] 内

- -1000 <= Node.val <= 1000
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

    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [3,9,20,null,null,15,7]
    # 期望输出：[[3],[9,20],[15,7]]
    print(s.levelOrder(list_to_tree([3,9,20,None,None,15,7])))

    # 示例 2：输入 root = [1]
    # 期望输出：[[1]]
    print(s.levelOrder(list_to_tree([1])))

    # 示例 3：输入 root = []
    # 期望输出：[]
    print(s.levelOrder(list_to_tree([])))
