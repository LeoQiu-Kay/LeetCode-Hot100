"""
437. 路径总和 III
难度：中等
链接：https://leetcode.cn/problems/path-sum-iii/

给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：

    输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    输出：3
    解释：和等于 8 的路径有 3 条，如图所示。

示例 2：

    输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    输出：3

提示:

- 二叉树的节点个数的范围是 [0,1000]

- -10⁹ <= Node.val <= 10⁹

- -1000 <= targetSum <= 1000
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

    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    # 期望输出：3
    print(s.pathSum(list_to_tree([10,5,-3,3,2,None,11,3,-2,None,1]), 8))

    # 示例 2：输入 root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    # 期望输出：3
    print(s.pathSum(list_to_tree([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22))
