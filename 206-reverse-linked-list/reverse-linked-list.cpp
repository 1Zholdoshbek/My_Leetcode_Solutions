/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        struct ListNode* a=NULL;
        struct ListNode* b=head;
        struct ListNode* next;
        while(b!=NULL){
            next=b->next;
            b->next=a;
            a=b;
            b=next;
        }
        head=a;
        return head;
    }
};