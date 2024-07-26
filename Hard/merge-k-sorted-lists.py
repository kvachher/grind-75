class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for l in lists : 
            ptr = l
            while ptr : 
                heappush(heap, ptr.val)
                ptr = ptr.next
        head = ListNode(0)
        curr = head
        while curr and heap:
            curr.next = ListNode(heappop(heap))
            curr = curr.next
        return head.next
