# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = ListNode()
        newListHead = newList

        while l1 and l2:
            if (l1.val <= l2.val):
                # print(l1.val)
                newList.next = ListNode(l1.val)
                l1 = l1.next
            else:
                # print(l2.val)
                newList.next = ListNode(l2.val)
                l2 = l2.next
            newList = newList.next

        while l1:
            # print(l1.val)
            newList.next = ListNode(l1.val)
            newList = newList.next
            l1 = l1.next

        while l2:
            # print(l2.val)
            newList.next = ListNode(l2.val)
            newList = newList.next
            l2 = l2.next

        return newListHead.next


l1 = ListNode(1)
l1.next = ListNode(2)
# l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

result = Solution().mergeTwoLists(l1, l2)

print()

while result:
    print(result.val)
    result = result.next
