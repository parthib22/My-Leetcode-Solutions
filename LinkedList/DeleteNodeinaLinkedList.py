# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Daily 05.05.2024

# 237. Delete Node in a Linked List

# There is a singly-linked list head and we want to delete a node node in it.

# You are given the node to be deleted node. You will not be given access to the first node of head.

# All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

# Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

# The value of the given node should not exist in the linked list.
# The number of nodes in the linked list should decrease by one.
# All the values before node should be in the same order.
# All the values after node should be in the same order.
# Custom testing:

# For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
# We will build the linked list and pass the node to your function.
# The output will be the entire list after calling your function.


# Example 1:
# https://assets.leetcode.com/uploads/2020/09/01/node1.jpg
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

# Example 2:
# https://assets.leetcode.com/uploads/2020/09/01/node2.jpg
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

# Constraints:
# The number of the nodes in the given list is in the range [2, 1000].
# -1000 <= Node.val <= 1000
# The value of each node in the list is unique.
# The node to be deleted is in the list and is not a tail node.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # while node.next:
        #     node.val = node.next.val
        #     temp = node
        #     node = node.next

        # temp.next = None

        node.val, node.next = node.next.val, node.next.next


def createLinkedList(list):
    head = ListNode(list[0])
    temp = head
    for i in range(1, len(list)):
        temp.next = ListNode(list[i])
        temp = temp.next
    return head


def getNode(head, val):
    while head:
        if head.val == val:
            return head
        head = head.next


def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    list = list(map(int, input().split()))
    val = int(input())
    head = createLinkedList(list)
    node = getNode(head, val)
    Solution().deleteNode(node)
    printList(head)
