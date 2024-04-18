# https://leetcode.com/problems/add-two-numbers/

# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1 = ""
        n2 = ""

        start = l1
        while start:
            n1 = str(start.val) + n1
            start = start.next

        start = l2
        while start:
            n2 = str(start.val) + n2
            start = start.next

        _sum = str(int(n1) + int(n2))

        start = ListNode(_sum[-1])
        head = start
        for i in range(2, len(_sum) + 1):
            start.next = ListNode(_sum[-i])
            start = start.next

        return head


def printList(l: Optional[ListNode]) -> None:
    start = l
    while start:
        print(start.val, end=" ")
        start = start.next
    print()


def createListNode(l: list) -> Optional[ListNode]:
    start = ListNode(l[0])
    head = start
    for i in range(1, len(l)):
        start.next = ListNode(l[i])
        start = start.next
    return head


if __name__ == "__main__":

    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    l1 = createListNode(l1)
    l2 = createListNode(l2)

    printList(Solution().addTwoNumbers(l1, l2))
