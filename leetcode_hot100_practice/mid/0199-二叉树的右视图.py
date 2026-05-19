"""
199. 二叉树的右视图
难度：中等
链接：https://leetcode.cn/problems/binary-tree-right-side-view/

给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1：

输入： root = [1,2,3,null,5,null,4]

输出： [1,3,4]

解释：

示例 2：

输入： root = [1,2,3,4,null,null,null,5]

输出： [1,3,4,5]

解释：

示例 3：

输入： root = [1,null,3]

输出： [1,3]

示例 4：

输入： root = []

输出： []

提示:

- 二叉树的节点个数的范围是 [0,100]

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

    def rightSideView(self, root: TreeNode | None) -> list[int]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [1,2,3,null,5,null,4]
    # 期望输出：[1,3,4]
    print(s.rightSideView(list_to_tree([1,2,3,None,5,None,4])))

    # 示例 2：输入 root = [1,2,3,4,null,null,null,5]
    # 期望输出：[1,3,4,5]
    print(s.rightSideView(list_to_tree([1,2,3,4,None,None,None,5])))

    # 示例 3：输入 root = [1,null,3]
    # 期望输出：[1,3]
    print(s.rightSideView(list_to_tree([1,None,3])))

    # 示例 4：输入 root = []
    # 期望输出：[]
    print(s.rightSideView(list_to_tree([])))
