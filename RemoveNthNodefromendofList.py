# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = -n
        start = head
        while start:
            pointer = pointer + 1
            start = start.next

        if pointer == 0:
            return head.next

        start = head

        for _ in range(pointer - 1):
            start = start.next

        start.next = start.next.next

        return head


def printList(l: Optional[ListNode]) -> None:
    start = l
    while start:
        print(start.val, end=" ")
        start = start.next
    print()


def createListNode(l: list) -> Optional[ListNode]:
    head = ListNode(l[0])
    start = head
    for i in range(1, len(l)):
        start.next = ListNode(l[i])
        start = start.next
    return head


if __name__ == "__main__":
    l = list(map(int, input().split()))
    n = int(input())
    head = createListNode(l)
    printList(Solution().removeNthFromEnd(head, n))
