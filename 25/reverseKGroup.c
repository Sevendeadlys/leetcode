/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverse(struct ListNode* head);
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    struct ListNode *pre,*p,*start,*end,*ret;
    int count = k;
    pre = (struct ListNode*)malloc(4);
    start = end = p = head;
    ret = pre;
    while(p){
        end = p;
        p = p->next;
        count --;
        if(count == 0){
            end->next = NULL;
            pre->next = reverse(start);
            pre = start;
            start = p;
            count = k;
        }
    }
    if(start == head) return free(ret),head;
    pre->next = start;
    pre = ret->next;
    return free(ret),pre;
}

struct ListNode* reverse(struct ListNode* head){
    struct ListNode* p,*pre,*next;
    if(!head||!head->next) return head;
    pre = head;
    p = head->next;
    while(p&&p->next){
        next = p->next;
        p->next = pre;
        pre = p;
        p = next;
    }
    p->next = pre;
    return p;
}
