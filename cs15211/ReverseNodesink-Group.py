__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reverse-nodes-in-k-group.py
# Time:  O(n)
# Space: O(1)
# LinkedList
#
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# You may not alter the values in the nodes, only nodes itself may be changed.
#
# Only constant memory is allowed.
#
# For example,
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
# Microsoft Facebook

import unittest
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object, unittest.TestCase):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur:
            nextHead = cur.next
            nextTail = cur
            for i in xrange(k):
                nextTail = nextTail.next
                if not nextTail:
                    return dummy.next
            nextNextHead = nextTail.next
            nextTail.next = None
            cur.next = None
            cur.next = self.reverse(nextHead)
            nextHead.next = nextNextHead
            cur = nextHead


        return dummy.next


    def reverse(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def test(self):
        self.assertTrue()



if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().reverseKGroup(head, 4)
    #print Solution().reverseKGroupif(head, 1)



# http://www.cnblogs.com/zuoyuan/p/3785555.html
class SolutionOther:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverse(self, start, end):
        newhead = ListNode(0)
        newhead.next = start
        while newhead.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = newhead.next
            newhead.next = tmp
        return (end, start)


    def reverseKGroup(self, head, k):
        if head == None:
            return head

        nhead = ListNode(0)
        nhead.next = head
        start = nhead

        while start.next:
            end = start
            for i in range(k-1):
                end = end.next
                if end.next == None:
                    return nhead.next

            res = self.reverse(start.next, end.next)
            start.next = res[0]
            start = res[1]
        return nhead.next

#test
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8)
l1.next = l2; l2.next = l3 ; l3.next = l4 ; l4.next = l5 ; l5.next = l6 ; l6.next = l7 ; l7.next = l8

#test
#test = SolutionOther()
#nh = test.reverseKGroup(l1, 3)
#while nh:
#    print nh.val
#    nh = nh.next

#java
js = '''
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (k < 2) {
            return head;
        }
        ListNode fakeHead = new ListNode(0);
        fakeHead.next = head;
        ListNode cur = fakeHead;
        while (cur != null) {
            ListNode nextHead = cur.next;
            ListNode nextTail = cur;
            for (int i = 0; i < k; i++) {
                nextTail = nextTail.next;
                if (nextTail == null) {
                    return fakeHead.next;
                }
            }
            ListNode nextNextHead = nextTail.next;
            cur.next = null;
            nextTail.next = null;
            cur.next = reverse(nextHead);
            nextHead.next = nextNextHead;
            cur = nextHead;
        }
        return fakeHead.next;
    }

    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
}
'''