# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(1)
# list2 = ListNode(1)
# list2.next = ListNode(2)
# list2.next.next = ListNode(4)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        # print(l1)
        if curr1 is None and curr2 is None:
            return

        if curr1 is None:
            if curr2 is not None:
                ln = ListNode(curr2.val)
                curr2 = curr2.next
        elif curr2 is None:
            if curr1 is not None:
                ln = ListNode(curr1.val)
                curr1 = curr1.next
        elif curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                ln = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                ln = ListNode(curr2.val)
                curr2 = curr2.next
        curr_ln = ln

        while curr1 is not None or curr2 is not None:
            if curr1 is not None and curr2 is not None:
                if curr1.val <= curr2.val:
                    curr_ln.next = ListNode(curr1.val)
                    curr_ln = curr_ln.next
                    curr1 = curr1.next
                else:

                    curr_ln.next = ListNode(curr2.val)
                    curr2 = curr2.next
                    curr_ln = curr_ln.next
            else:

                if curr1 is not None and curr2 is None:
                    curr_ln.next = ListNode(curr1.val)
                    curr_ln = curr_ln.next
                    curr1 = curr1.next

                elif curr2 is not None and curr1 is None:

                    curr_ln.next = ListNode(curr2.val)
                    curr2 = curr2.next
                    curr_ln = curr_ln.next

        print(ln)
        return ln
