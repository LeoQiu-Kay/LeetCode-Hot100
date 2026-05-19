"""
19. 删除链表的倒数第 N 个结点
难度：中等
链接：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：

    输入：head = [1,2,3,4,5], n = 2
    输出：[1,2,3,5]

示例 2：

    输入：head = [1], n = 1
    输出：[]

示例 3：

    输入：head = [1,2], n = 1
    输出：[1]

提示：

- 链表中结点的数目为 sz

- 1 <= sz <= 30

- 0 <= Node.val <= 100

- 1 <= n <= sz

进阶： 你能尝试使用一趟扫描实现吗？
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

    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 head = [1,2,3,4,5], n = 2
    # 期望输出：[1,2,3,5]
    print(s.removeNthFromEnd(list_to_listnode([1,2,3,4,5]), 2))

    # 示例 2：输入 head = [1], n = 1
    # 期望输出：[]
    print(s.removeNthFromEnd(list_to_listnode([1]), 1))

    # 示例 3：输入 head = [1,2], n = 1
    # 期望输出：[1]
    print(s.removeNthFromEnd(list_to_listnode([1,2]), 1))
