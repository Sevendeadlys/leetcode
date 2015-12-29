/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode *pre,*curr,*next,*phead;

    if(!head || !head->next) return head;

    pre = head;
    curr = head->next;

    head = curr;

    while(curr){
        phead = pre;
        next = curr->next;
        curr->next = pre;
        pre->next = next;
        if(!next || !next->next) return head;
        pre = pre->next;
        curr = pre->next;
        phead->next = curr;
    }
    return head;
}
