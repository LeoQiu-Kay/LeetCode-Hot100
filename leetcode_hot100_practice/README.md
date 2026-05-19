# Hot 100 刷题骨架

每道题一份 `.py`，结构如下：

1. **顶部 docstring**：题号、难度、链接、完整题面（描述 / 示例 / 提示）
2. **辅助类**：如果题目涉及链表（`ListNode`）、二叉树（`TreeNode`）或带 random 指针的节点（`Node`），自动注入对应类定义和**输入构造工具函数**：
   - `list_to_listnode([1,2,3])` → `ListNode`
   - `listnode_to_list(head)` → list（方便 print 对比）
   - `list_to_tree([1, None, 2, 3])` → `TreeNode`（按 LeetCode 层序数组）
3. **`class Solution`**：方法签名保留，方法体被替换为 `raise NotImplementedError` —— 这是你要补的核心代码
4. **`if __name__ == "__main__":`**：自动按题面"示例"区生成测试调用，每个示例附带：
   - 输入注释
   - 期望输出注释
   - `print(s.method(...))` 实际调用

## 用法

1. 选一道题打开（比如 `simple/0001-两数之和.py`）
2. 把 `raise NotImplementedError` 替换成你的实现
3. `python "simple/0001-两数之和.py"` 直接跑，比对输出和注释里的期望值

填好实现后立刻能跑，不必再手写测试样板。

## 几种特殊题型

- **链表题**（21、206、141、19、142、146 等）：方法的入参类型是 `ListNode`，main 块里用 `list_to_listnode([...])` 把 Python list 包成链表。返回链表时建议你在实现末尾用 `listnode_to_list(head)` 转回 list 再 return，这样 `print` 能直接看结果。
- **二叉树题**（94、104、226 等）：用 `list_to_tree([...])` 构造，`None` 表示空孩子。
- **设计题**（146 LRU、155 最小栈、208 Trie、295 中位数、460 等）：main 块里没法自动模拟操作序列，留了 TODO 注释 + LeetCode 原始示例文本，你自己照着写几行调用即可。

## 与其它目录的关系

```
leetcode_hot100/             # 题面 + 题解（参考答案）
└── simple/0001-两数之和.md  ← 卡壳时偷看

leetcode_hot100_practice/    # 你来写
└── simple/0001-两数之和.py  ← 在这里填代码
```

建议先尝试 `practice` 文件，搞不定再去 `leetcode_hot100/` 对应 md 查参考实现 + 直觉类比。
