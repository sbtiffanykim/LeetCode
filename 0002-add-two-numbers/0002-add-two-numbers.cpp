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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // create dummy to store answer
        ListNode* dummy = new ListNode();
        ListNode *node = dummy;
        
        int flag = 0;  // 1 if sum >= 10
        while (l1 != nullptr || l2 != nullptr || flag) {
            // add numbers
            int val1 = (l1 != nullptr) ? l1->val : 0;
            int val2 = (l2 != nullptr) ? l2->val : 0;
            int val = val1 + val2 + flag;
            flag = val / 10;
            val %= 10;
            node->next = new ListNode(val);
            
            // update pointers
            l1 = (l1 != nullptr) ? l1->next : nullptr;
            l2 = (l2 != nullptr) ? l2->next : nullptr;
            node = node->next;
        }
        return dummy->next;
    }
};