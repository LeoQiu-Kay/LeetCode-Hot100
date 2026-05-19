"""
148. 排序链表
难度：中等
链接：https://leetcode.cn/problems/sort-list/

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例 1：

    输入：head = [4,2,1,3]
    输出：[1,2,3,4]

示例 2：

    输入：head = [-1,5,3,4,0]
    输出：[-1,0,3,4,5]

示例 3：

    输入：head = []
    输出：[]

提示：

- 链表中节点的数目在范围 [0, 5 * 10⁴] 内

- -10⁵ <= Node.val <= 10⁵

进阶： 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
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

    def sortList(self, head: ListNode | None) -> ListNode | None:
        raise NotImplementedError

    def _merge(self, a: ListNode | None, b: ListNode | None) -> ListNode | None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 head = [4,2,1,3]
    # 期望输出：[1,2,3,4]
    print(s.sortList(list_to_listnode([4,2,1,3])))

    # 示例 2：输入 head = [-1,5,3,4,0]
    # 期望输出：[-1,0,3,4,5]
    print(s.sortList(list_to_listnode([-1,5,3,4,0])))

    # 示例 3：输入 head = []
    # 期望输出：[]
    print(s.sortList(list_to_listnode([])))
