/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    struct ListNode *tail;
    if(!head) return head;
    int len = 1;
    tail = head;
    while(tail->next){
        len++;
        tail = tail->next;
    }
    tail->next = head;
    if(k %= len){
        k = len - k;
        for(;k > 0;k--) tail = tail->next;
    }

    head = tail->next;
    tail->next = NULL;
    return head;
}
