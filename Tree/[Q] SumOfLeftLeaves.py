# https://leetcode.com/problems/sum-of-left-leaves/

# 404. Sum of Left Leaves

# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

# Example 1:
# https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# Example 2:
# Input: root = [1]
# Output: 0

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0

        def dfs(root, flag):
            nonlocal sum
            if not root:
                return
            if not root.left and not root.right and flag:
                sum += root.val
            dfs(root.left, True)
            dfs(root.right, False)

        dfs(root, None)
        return sum


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
    root = buildTree(arr, len(arr))
    print(Solution().sumOfLeftLeaves(root))
