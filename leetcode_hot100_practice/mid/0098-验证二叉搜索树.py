"""
98. 验证二叉搜索树
难度：中等
链接：https://leetcode.cn/problems/validate-binary-search-tree/

给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

- 节点的左子树只包含 严格小于 当前节点的数。

- 节点的右子树只包含 严格大于 当前节点的数。

- 所有左子树和右子树自身必须也是二叉搜索树。

示例 1：

    输入：root = [2,1,3]
    输出：true

示例 2：

    输入：root = [5,1,4,null,null,3,6]
    输出：false
    解释：根节点的值是 5 ，但是右子节点的值是 4 。

提示：

- 树中节点数目范围在[1, 10⁴] 内

- -2³¹ <= Node.val <= 2³¹ - 1
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

    def isValidBST(self, root: TreeNode | None) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [2,1,3]
    # 期望输出：true
    print(s.isValidBST(list_to_tree([2,1,3])))

    # 示例 2：输入 root = [5,1,4,null,null,3,6]
    # 期望输出：false
    print(s.isValidBST(list_to_tree([5,1,4,None,None,3,6])))
