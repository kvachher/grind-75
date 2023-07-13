/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {

        if (head == null)
            return false;
        
       ListNode tortoise = head;
       ListNode hare = head.next;

       while (tortoise != hare) {

           if (hare == null || hare.next == null) {
               return false;
           }
           tortoise = tortoise.next;
           hare = hare.next.next;
       }
        return true;
    }
}
