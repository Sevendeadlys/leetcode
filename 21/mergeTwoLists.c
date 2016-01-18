/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *head;
    struct ListNode *tail = (struct ListNode *)malloc(sizeof(struct ListNode));
    head = tail;
    
    while(l1&&l2){
        if(l1->val < l2->val){
            tail->next = l1;
            l1 = l1->next;
        }
        else{
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }
    tail->next = l1?l1:l2;
    struct ListNode *temp = head;
    head = head->next;
    free(temp);
    return head;
}