"""
114. 二叉树展开为链表
难度：中等
链接：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/

给你二叉树的根结点 root ，请你将它展开为一个单链表：

- 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。

- 展开后的单链表应该与二叉树 先序遍历 顺序相同。

示例 1：

    输入：root = [1,2,5,3,4,null,6]
    输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：

    输入：root = []
    输出：[]

示例 3：

    输入：root = [0]
    输出：[0]

提示：

- 树中结点数在范围 [0, 2000] 内

- -100 <= Node.val <= 100

进阶： 你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
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

    def flatten(self, root: TreeNode | None) -> None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 root = [1,2,5,3,4,null,6]
    # 期望输出：[1,null,2,null,3,null,4,null,5,null,6]
    print(s.flatten(list_to_tree([1,2,5,3,4,None,6])))

    # 示例 2：输入 root = []
    # 期望输出：[]
    print(s.flatten(list_to_tree([])))

    # 示例 3：输入 root = [0]
    # 期望输出：[0]
    print(s.flatten(list_to_tree([0])))
