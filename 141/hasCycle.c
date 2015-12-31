/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *p,*q;
    p = q = head;

    while(p && p->next)
    {
        p = p->next->next;
        q = q->next;
        if(p == q) return true;
    }
    
    return false;
}
