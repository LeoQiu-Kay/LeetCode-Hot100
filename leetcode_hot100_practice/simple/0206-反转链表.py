"""
206. 反转链表
难度：简单
链接：https://leetcode.cn/problems/reverse-linked-list/

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：

    输入：head = [1,2,3,4,5]
    输出：[5,4,3,2,1]

示例 2：

    输入：head = [1,2]
    输出：[2,1]

示例 3：

    输入：head = []
    输出：[]

提示：

- 链表中节点的数目范围是 [0, 5000]

- -5000 <= Node.val <= 5000

进阶： 链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
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

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 head = [1,2,3,4,5]
    # 期望输出：[5,4,3,2,1]
    print(s.reverseList(list_to_listnode([1,2,3,4,5])))

    # 示例 2：输入 head = [1,2]
    # 期望输出：[2,1]
    print(s.reverseList(list_to_listnode([1,2])))

    # 示例 3：输入 head = []
    # 期望输出：[]
    print(s.reverseList(list_to_listnode([])))
