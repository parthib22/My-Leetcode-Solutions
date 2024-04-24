# https://leetcode.com/problems/merge-k-sorted-lists/

# 23. Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merge = []

        for _list in lists:
            while _list:
                merge.append(_list.val)
                _list = _list.next

        merge.sort()

        dummy = ListNode()
        mergedList = dummy

        for value in merge:
            mergedList.next = ListNode(value)
            mergedList = mergedList.next

        return dummy.next


if __name__ == "__main__":

    def createList(list: List[int]) -> Optional[ListNode]:
        _list = ListNode()
        newList = _list

        for value in list:
            newList.next = ListNode(value)
            newList = newList.next

        return _list.next

    def printList(list: Optional[ListNode]) -> None:
        while list:
            print(list.val, end=" ")
            list = list.next
        print()

    k = int(input())
    lists = [createList(list(map(int, input().split()))) for _ in range(k)]

    result = Solution().mergeKLists(lists)
    printList(result)
