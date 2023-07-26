/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* recurse(struct ListNode* prev, struct ListNode* curr,      struct ListNode* next) {
    if (curr == NULL)
        return prev;
    next = curr->next;
    curr->next = prev;
    return recurse(curr, next, NULL);
}
struct ListNode* reverseList(struct ListNode* head){
    if (head == NULL)
        return NULL;
    return recurse(NULL, head, NULL);
}
