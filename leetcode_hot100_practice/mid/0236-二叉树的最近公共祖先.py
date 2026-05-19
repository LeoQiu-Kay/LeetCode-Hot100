"""
236. 二叉树的最近公共祖先
难度：中等
链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 1：

    输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    输出：3
    解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：

    输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    输出：5
    解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：

    输入：root = [1,2], p = 1, q = 2
    输出：1

提示：

- 树中节点数目在范围 [2, 10⁵] 内。

- -10⁹ <= Node.val <= 10⁹

- 所有 Node.val 互不相同 。

- p != q

- p 和 q 均存在于给定的二叉树中。
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

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    # 期望输出：3
    print(s.lowestCommonAncestor(list_to_tree([3,5,1,6,2,0,8,None,None,7,4]), 5, 1))

    # 示例 2：输入 root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    # 期望输出：5
    print(s.lowestCommonAncestor(list_to_tree([3,5,1,6,2,0,8,None,None,7,4]), 5, 4))

    # 示例 3：输入 root = [1,2], p = 1, q = 2
    # 期望输出：1
    print(s.lowestCommonAncestor(list_to_tree([1,2]), 1, 2))
