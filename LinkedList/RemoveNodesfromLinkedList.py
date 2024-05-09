# https://leetcode.com/problems/remove-nodes-from-linked-list/description/?envType=daily-question&envId=2024-05-06

# Daily 06.05.2024

# 2487. Remove Nodes From Linked List

# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to the right side of it.

# Return the head of the modified linked list.

# Example 1:
# https://assets.leetcode.com/uploads/2022/10/02/drawio.png
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.

# Example 2:
# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.

# Constraints:
# The number of the nodes in the given list is in the range [1, 105].
# 1 <= Node.val <= 105


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = start = head

        # while start:
        #     ptr = start
        #     while ptr and start.val >= ptr.val:
        #         ptr = ptr.next
        #     if ptr:
        #         if start == head:
        #             head = start.next
        #             prev = head
        #         else:
        #             prev.next = start.next
        #             prev = start
        #     start = start.next

        start = head

        stack = []

        while start:
            while stack and stack[-1] < start.val:
                stack.pop()
            stack.append(start.val)
            start = start.next

        # print(stack)

        _next = None
        while stack:
            start = ListNode(stack.pop())
            start.next = _next
            _next = start

        return _next


def createList(arr):
    head = ListNode(arr[0])
    start = head
    for i in range(1, len(arr)):
        start.next = ListNode(arr[i])
        start = start.next
    return head


def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    head = list(map(int, input().split()))
    head = createList(head)
    printList(Solution().removeNodes(head))
