# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def print_ll(node):
    while node!=None:
        print(node.val)
        node = node.next
    print('...')

def reverse(head):
    if head == None:
        return None

    if head.next == None:
        return head
    curr = head.next
    prev = head
    head.next=None
    while(True):
        if curr == None:
            break
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev


class Solution(object):

    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        '''
        0 1 2 3 4 5 6 7
        0 7 1 6 2 5 3 4

        identify middle
        0 1 2 3
        4 5 6 7

        reverse second list:
        7 6 5 4

        interleave:
        '''
                fast = head
        slow = head
        while True:

            fast = fast.next
            if fast!=None:
                fast = fast.next

            if fast == None:
                break
            slow = slow.next
        # Now slow is in the middle
        #print_ll(head)
        #print_ll(slow)
        '''
        1 2 3 4
          ^
        1 2 3 4 5
            ^
        '''

        second = slow.next
        slow.next = None
        first = head

        rev_sec = reverse(second)
        #print_ll(rev_sec)

        ptr1 = head 
        ptr2 = rev_sec 
        while(True): 
            if ptr2 == None: 
                break 
        '''
        p1->p1next
        p2->p2next
        '''
        ptr1_next = ptr1.next
        ptr2_next = ptr2.next
        ptr2.next = ptr1_next

        '''
        p1->p1next
        p2->p1next
        '''
        ptr1.next = ptr2
        '''
        p1->p2->p1next
        '''
        ptr2 = ptr2_next
        ptr1 = ptr1_next


