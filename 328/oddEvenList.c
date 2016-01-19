/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) {
    struct ListNode *p,*q,*pre;

    if(!head || !head->next || !head->next->next){
        return head;
    }
    p = head;
    pre = head->next;
    q = pre->next;

    while(q){
        pre->next = q->next;
        q->next = p->next;
        p->next = q;
        if(!pre->next||!pre->next->next) return head;
        p = p->next;
        pre = pre->next;
        q = pre->next;
    }
    return head;
}
