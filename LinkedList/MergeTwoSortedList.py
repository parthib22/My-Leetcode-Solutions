# https://leetcode.com/problems/merge-two-sorted-lists/

# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        newList = dummy

        while list1 and list2:

            if list1.val < list2.val:
                newList.next = list1
                list1 = list1.next

            else:
                newList.next = list2
                list2 = list2.next

            newList = newList.next

        newList.next = list1 if list1 else list2

        return dummy.next

        # def createList(list: Optional[ListNode]) -> List[int]:
        #     _list = []

        #     while list:
        #         _list.append(list.val)
        #         list = list.next

        #     return _list

        # _list1 = createList(list1)
        # _list2 = createList(list2)

        # _newList = sorted(_list1 + _list2)

        # dummy = ListNode()
        # newList = dummy

        # for _new in _newList:
        #     newList.next = ListNode(_new)
        #     newList = newList.next

        # return dummy.next


def createNode(_list: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    newList = dummy

    for i in _list:
        newList.next = ListNode(i)
        newList = newList.next

    return dummy.next


if __name__ == "__main__":
    _list1 = list(map(int, input().split()))
    _list2 = list(map(int, input().split()))

    list1 = createNode(_list1)
    list2 = createNode(_list2)

    newList = Solution().mergeTwoLists(list1, list2)
    while newList:
        print(newList.val, end=" ")
        newList = newList.next
