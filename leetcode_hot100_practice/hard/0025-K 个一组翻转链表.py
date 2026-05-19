"""
25. K 个一组翻转链表
难度：困难
链接：https://leetcode.cn/problems/reverse-nodes-in-k-group/

给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

示例 1：

    输入：head = [1,2,3,4,5], k = 2
    输出：[2,1,4,3,5]

示例 2：

    输入：head = [1,2,3,4,5], k = 3
    输出：[3,2,1,4,5]

提示：

- 链表中的节点数目为 n

- 1 <= k <= n <= 5000

- 0 <= Node.val <= 1000

进阶： 你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
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

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 head = [1,2,3,4,5], k = 2
    # 期望输出：[2,1,4,3,5]
    print(s.reverseKGroup(list_to_listnode([1,2,3,4,5]), 2))

    # 示例 2：输入 head = [1,2,3,4,5], k = 3
    # 期望输出：[3,2,1,4,5]
    print(s.reverseKGroup(list_to_listnode([1,2,3,4,5]), 3))
