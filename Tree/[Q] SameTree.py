# https://leetcode.com/problems/same-tree/

# 100. Same Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if (not p and q) or (not q and p):
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def buildTree(arr: list, n: int) -> Optional[TreeNode]:
    if not arr:
        return None
    root = TreeNode(int(arr[0]))
    queue = [root]
    i = 1
    while i < n:
        node = queue.pop(0)
        if node:
            if i < n and arr[i] != "null":
                node.left = TreeNode(int(arr[i]))
                queue.append(node.left)
            i += 1
            if i < n and arr[i] != "null":
                node.right = TreeNode(int(arr[i]))
                queue.append(node.right)
            i += 1
    return root


if __name__ == "__main__":
    arr1 = list(map(str, input().split()))
    arr2 = list(map(str, input().split()))
    p = buildTree(arr1, len(arr1))
    q = buildTree(arr2, len(arr2))
    print(Solution().isSameTree(p, q))
