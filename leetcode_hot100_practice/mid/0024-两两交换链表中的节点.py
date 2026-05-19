"""
24. 两两交换链表中的节点
难度：中等
链接：https://leetcode.cn/problems/swap-nodes-in-pairs/

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

示例 1：

    输入：head = [1,2,3,4]
    输出：[2,1,4,3]

示例 2：

    输入：head = []
    输出：[]

示例 3：

    输入：head = [1]
    输出：[1]

提示：

- 链表中节点的数目在范围 [0, 100] 内

- 0 <= Node.val <= 100
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_listnode(items):
    """把 Python list 转成单链表，返回头节点。"""
    dummy = ListNode()
    cur = dummy
    for x in items:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def listnode_to_list(head):
    """把单链表转回 Python list，方便打印对比。"""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class Solution:

    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 head = [1,2,3,4]
    # 期望输出：[2,1,4,3]
    print(s.swapPairs(list_to_listnode([1,2,3,4])))

    # 示例 2：输入 head = []
    # 期望输出：[]
    print(s.swapPairs(list_to_listnode([])))

    # 示例 3：输入 head = [1]
    # 期望输出：[1]
    print(s.swapPairs(list_to_listnode([1])))
