"""
234. 回文链表
难度：简单
链接：https://leetcode.cn/problems/palindrome-linked-list/

给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

示例 1：

    输入：head = [1,2,2,1]
    输出：true

示例 2：

    输入：head = [1,2]
    输出：false

提示：

- 链表中节点数目在范围[1, 10⁵] 内

- 0 <= Node.val <= 9

进阶： 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
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

    def isPalindrome(self, head: ListNode | None) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    # 示例 1：输入 head = [1,2,2,1]
    # 期望输出：true
    print(s.isPalindrome(list_to_listnode([1,2,2,1])))

    # 示例 2：输入 head = [1,2]
    # 期望输出：false
    print(s.isPalindrome(list_to_listnode([1,2])))
