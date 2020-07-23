class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head

        previous = dummy
        while previous.next != None and previous.next.next:
            node1 = previous.next
            node2 = previous.next.next
            previous.next = node2
            node1.next = node2.next
            node2.next = node1
            previous = node1

        return dummy.next