/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ArrayList<Integer> mergedList = new ArrayList<>();

        traverse(list1, mergedList);
        traverse(list2, mergedList);

        sortList(mergedList);
        
        if (mergedList.isEmpty())
            return null; 
        
        ListNode sorted = new ListNode(mergedList.get(0));
        ListNode curr = sorted;

        for (int i = 1; i < mergedList.size(); i++) {
            curr.next = new ListNode(mergedList.get(i));
            curr = curr.next;
        }

        return sorted;
    }

    public void traverse(ListNode travel, ArrayList list) {
        while (travel != null) { 
            list.add(travel.val);
            travel = travel.next;
        }
    }

    public void sortList(ArrayList<Integer> list) {
    for (int i = 0; i < list.size(); i++) {
        for (int j = i + 1; j < list.size(); j++) {
            if (list.get(i) > list.get(j)) {
                int temp = list.get(i);
                list.set(i, list.get(j));
                list.set(j, temp);
            }
        }
    }
}
}
