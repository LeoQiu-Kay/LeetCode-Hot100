"""
141. 环形链表
难度：简单
链接：https://leetcode.cn/problems/linked-list-cycle/

给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

如果链表中存在环 ，则返回 true 。 否则，返回 false 。

示例 1：

    输入：head = [3,2,0,-4], pos = 1
    输出：true
    解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：

    输入：head = [1,2], pos = 0
    输出：true
    解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：

    输入：head = [1], pos = -1
    输出：false
    解释：链表中没有环。

提示：

- 链表中节点的数目范围是 [0, 10⁴]

- -10⁵ <= Node.val <= 10⁵

- pos 为 -1 或者链表中的一个 有效索引 。

进阶： 你能用 O(1)（即，常量）内存解决此问题吗？
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

    def hasCycle(self, head: ListNode | None) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 head = [3,2,0,-4], pos = 1
    # 期望输出：true
    print(s.hasCycle(list_to_listnode([3,2,0,-4]), 1))

    # 示例 2：输入 head = [1,2], pos = 0
    # 期望输出：true
    print(s.hasCycle(list_to_listnode([1,2]), 0))

    # 示例 3：输入 head = [1], pos = -1
    # 期望输出：false
    print(s.hasCycle(list_to_listnode([1]), -1))
