/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 /*
 * traverse the linklist, add each corresponding node value.
 * the carry_bit is the important thing 
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *head,*tail,*pl1,*pl2;
    int carry_bit = 0;
    int sum = 0;

    if(!l1) return l2;
    if(!l2) return l1;

    head = tail = (struct ListNode*)malloc(sizeof(struct ListNode));
    pl1 = l1;
    pl2 = l2;
    while(pl1 && pl2)
    {
        tail->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        tail = tail->next;
        tail->next = NULL;
        sum = pl1->val + pl2->val + carry_bit;
        carry_bit = sum/10;
        sum = sum%10;
        tail->val = sum;
        pl1 = pl1->next;
        pl2 = pl2->next;
    }
    if(pl1 || pl2) tail->next = (!pl1?pl2:pl1);
    while(carry_bit){
        if(tail->next){
            tail = tail->next;
            sum = tail->val + carry_bit;
            tail->val = sum%10;
            carry_bit = sum/10;
        }
        else{
            tail->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            tail = tail->next;
            tail->next = NULL;
            tail->val = carry_bit;
            carry_bit  = 0;
        }
    }
    tail = head;
    head = head->next;
    free(tail);
    return head;
}
