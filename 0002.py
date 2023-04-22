# Add Two Numbers
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    '''
    This class represents a node in a singly linked list. Each node has a value (val) and a reference to the next node (next).
    For example:
    >>> a = ListNode(1)
    >>> a.val
    1
    '''

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        This function takes in two linked lists (l1 and l2) as input and returns a new linked list that represents the sum of the two input linked lists. The function uses a dummy node to keep track of the head of the new linked list and a current node to keep track of the current node being processed. It also initializes a carry variable to 0.

        The function then loops through both input linked lists and the carry variable until all nodes have been processed. For each iteration, it adds the values of the current nodes in l1 and l2 (if they exist) to the carry variable. It then creates a new node in the output linked list with the value of carry % 10 (to handle cases where the sum is greater than 9) and sets the current node's next pointer to this new node. It then updates the current node to be the newly created node and updates the carry variable to be carry // 10 (to handle cases where the sum is greater than 9).

        Once all nodes have been processed, the function returns the next node after the dummy node, which represents the head of the new linked list.

        :param l1: The first linked list
        :param l2: The second linked list
        :return: The new linked list that represents the sum of the two input linked lists.
        :rtype: ListNode
        
        :Example:
        >>> l1 = ListNode(2, ListNode(4, ListNode(3)))
        >>> l2 = ListNode(5, ListNode(6, ListNode(4)))
        >>> Solution().addTwoNumbers(l1, l2)
        ListNode(7, ListNode(0, ListNode(8)))
        >>> l1 = ListNode(0)
        >>> l2 = ListNode(0)
        >>> Solution().addTwoNumbers(l1, l2)
        ListNode(0)
        >>> l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        >>> l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        >>> Solution().addTwoNumbers(l1, l2)
        '''
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10
        return dummy.next
