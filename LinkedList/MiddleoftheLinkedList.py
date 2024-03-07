from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start = head
        # c = 0
        # while start != None:
        #     c+=1
        #     start = start.next
        # start = head
        # for i in range(c//2):
        #     start = start.next
        # return start

        slowPointer = head
        fastPointer = head

        while fastPointer is not None and fastPointer.next is not None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        return slowPointer


if __name__ == "__main__":
    values = list(map(int, input().split()))

    # Create linked list from values
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    head = dummy.next
    dummy = None

    current = Solution().middleNode(head)

    output = []
    while current is not None:
        output.append(current.val)
        current = current.next

    print(output)
