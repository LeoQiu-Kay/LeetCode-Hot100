"""
92. 反转链表 II
难度：中等
链接：https://leetcode.cn/problems/reverse-linked-list-ii/

📌 不在 Hot 100 题单，作为 206 反转链表的进阶补充。

给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

示例 1：

    输入：head = [1,2,3,4,5], left = 2, right = 4
    输出：[1,4,3,2,5]

示例 2：

    输入：head = [5], left = 1, right = 1
    输出：[5]

提示：

- 链表中节点数目为 n
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

进阶：你可以使用一趟扫描完成反转吗？
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

    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 head = [1,2,3,4,5], left = 2, right = 4
    # 期望输出：[1,4,3,2,5]
    print(listnode_to_list(s.reverseBetween(list_to_listnode([1, 2, 3, 4, 5]), 2, 4)))

    # 示例 2：输入 head = [5], left = 1, right = 1
    # 期望输出：[5]
    print(listnode_to_list(s.reverseBetween(list_to_listnode([5]), 1, 1)))
