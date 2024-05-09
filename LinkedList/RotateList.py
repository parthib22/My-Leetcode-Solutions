# https://leetcode.com/problems/rotate-list/

# 61. Rotate List

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Constraints:
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0:
            return head

        size = 1
        end = head

        while end.next:
            size = size + 1
            end = end.next

        red = k % size

        if red == 0:
            return head

        mid = head

        for _ in range(size - red - 1):
            mid = mid.next

        beg = head
        head = mid.next
        mid.next = None
        end.next = beg

        return head


def createLinkedList(list):
    head = ListNode()
    temp = head
    for i in range(len(list)):
        temp.next = ListNode(list[i])
        temp = temp.next
    return head.next


def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    list = list(map(int, input().split()))
    k = int(input())
    head = createLinkedList(list)
    head = Solution().rotateRight(head, k)
    printList(head)
