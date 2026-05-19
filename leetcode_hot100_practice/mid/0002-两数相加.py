"""
2. 两数相加
难度：中等
链接：https://leetcode.cn/problems/add-two-numbers/

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：

    输入：l1 = [2,4,3], l2 = [5,6,4]
    输出：[7,0,8]
    解释：342 + 465 = 807.

示例 2：

    输入：l1 = [0], l2 = [0]
    输出：[0]

示例 3：

    输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    输出：[8,9,9,9,0,0,0,1]

提示：

- 每个链表中的节点数在范围 [1, 100] 内

- 0 <= Node.val <= 9

- 题目数据保证列表表示的数字不含前导零
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

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 l1 = [2,4,3], l2 = [5,6,4]
    # 期望输出：[7,0,8]
    print(s.addTwoNumbers(list_to_listnode([2,4,3]), list_to_listnode([5,6,4])))

    # 示例 2：输入 l1 = [0], l2 = [0]
    # 期望输出：[0]
    print(s.addTwoNumbers(list_to_listnode([0]), list_to_listnode([0])))

    # 示例 3：输入 l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # 期望输出：[8,9,9,9,0,0,0,1]
    print(s.addTwoNumbers(list_to_listnode([9,9,9,9,9,9,9]), list_to_listnode([9,9,9,9])))
