"""
124. 二叉树中的最大路径和
难度：困难
链接：https://leetcode.cn/problems/binary-tree-maximum-path-sum/

二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

示例 1：

    输入：root = [1,2,3]
    输出：6
    解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：

    输入：root = [-10,9,20,null,null,15,7]
    输出：42
    解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

提示：

- 树中节点数目范围是 [1, 3 * 10⁴]

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

    def maxPathSum(self, root: TreeNode | None) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [1,2,3]
    # 期望输出：6
    print(s.maxPathSum(list_to_tree([1,2,3])))

    # 示例 2：输入 root = [-10,9,20,null,null,15,7]
    # 期望输出：42
    print(s.maxPathSum(list_to_tree([-10,9,20,None,None,15,7])))
