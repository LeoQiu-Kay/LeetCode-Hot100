"""
21. 合并两个有序链表
难度：简单
链接：https://leetcode.cn/problems/merge-two-sorted-lists/

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：

    输入：l1 = [1,2,4], l2 = [1,3,4]
    输出：[1,1,2,3,4,4]

示例 2：

    输入：l1 = [], l2 = []
    输出：[]

示例 3：

    输入：l1 = [], l2 = [0]
    输出：[0]

提示：

- 两个链表的节点数目范围是 [0, 50]

- -100 <= Node.val <= 100

- l1 和 l2 均按 非递减顺序 排列
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

    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 l1 = [1,2,4], l2 = [1,3,4]
    # 期望输出：[1,1,2,3,4,4]
    print(s.mergeTwoLists(list_to_listnode([1,2,4]), list_to_listnode([1,3,4])))

    # 示例 2：输入 l1 = [], l2 = []
    # 期望输出：[]
    print(s.mergeTwoLists(list_to_listnode([]), list_to_listnode([])))

    # 示例 3：输入 l1 = [], l2 = [0]
    # 期望输出：[0]
    print(s.mergeTwoLists(list_to_listnode([]), list_to_listnode([0])))
