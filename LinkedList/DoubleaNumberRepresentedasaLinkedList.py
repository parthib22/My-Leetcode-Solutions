# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/?envType=daily-question&envId=2024-05-07

# Daily 07.05.2024

# 2816. Double a Number Represented as a Linked List

# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

# Return the head of the linked list after doubling it.

# Example 1:
# https://assets.leetcode.com/uploads/2023/05/28/example.png
# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

# Example 2:
# https://assets.leetcode.com/uploads/2023/05/28/example2.png
# Input: head = [9,9,9]
# Output: [1,9,9,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.

# Constraints:
# The number of nodes in the list is in the range [1, 104]
# 0 <= Node.val <= 9
# The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.

from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# sys.set_int_max_str_digits(20000)


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # start = head
        # num = ""

        # while start:
        #     num += str(start.val)
        #     start = start.next

        # num2 = str(int(num)*2)

        # # print(num2)

        # start = head
        # k = 0
        # while start:
        #     start.val = num2[k]
        #     k = k + 1
        #     temp = start
        #     start = start.next

        # if k < len(num2):
        #     temp.next = ListNode(num2[k])

        # return head

        #

        # def helper(node):
        #     num = node.val * 2
        #     if node.next:
        #         num += helper(node.next)

        #     node.val = num % 10
        #     return num // 10

        # carry = helper(head)
        # if carry == 0:
        #     return head
        # return ListNode(carry, head)

        #

        start = head
        store = deque()

        while start:
            store.append(start.val)
            start = start.next

        carry = 0
        for i in range(1, len(store) + 1):
            mul = store[-i] * 2
            store[-i] = (mul + carry) % 10
            carry = mul // 10

        if carry > 0:
            store.appendleft(carry)

        start = head

        while start:
            start.val = store.popleft()
            temp = start
            start = start.next

        if store:
            temp.next = ListNode(store.pop())

        return head


def createList(l: list[int]):
    head = ListNode(l[0])
    start = head
    for i in l[1:]:
        start.next = ListNode(i)
        start = start.next
    return head


def printList(head: Optional[ListNode]):
    start = head
    while start:
        print(start.val, end=" ")
        start = start.next


if __name__ == "__main__":
    l = list(map(int, input().split()))
    head = createList(l)
    printList(Solution().doubleIt(head))
