/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *p,*pre,*temp;

    if(!head || !head->next) return head;

    p = head->next;
    pre = head;
    while(p)
    {
        temp = p->next;
        p->next = pre;
        pre = p;
        p = temp;
    }
    head->next = NULL;
    head = pre;
    return head;
}
