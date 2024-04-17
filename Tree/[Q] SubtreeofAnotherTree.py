# https://leetcode.com/problems/subtree-of-another-tree/

# 572. Subtree of Another Tree

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:
# https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
# https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True

            if (not p and q) or (not q and p):
                return False

            if p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def dfs(root):
            if not root:
                return False

            if isSameTree(root, subRoot):
                return True

            return dfs(root.left) or dfs(root.right)

        return dfs(root)


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
    arr = list(map(str, input().split()))
    subArr = list(map(str, input().split()))
    root = buildTree(arr, len(arr))
    subRoot = buildTree(subArr, len(subArr))
    print(Solution().isSubtree(root, subRoot))
