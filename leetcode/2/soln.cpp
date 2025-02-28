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
        if (l1 == nullptr)
            return l2;
        if (l2 == nullptr)
            return l1;
        auto idx1 = l1;
        auto idx2 = l2;
        int carry = 0;
        int sum = 0;
        auto res = l1; // edit l1 in place
        int idx1val = 0, idx2val = 0;
        ListNode* tail_of_result = l1;
        while(true) {
            // exit criteria:
            // optimization: if one of them has run out and carry==0 we can exit by tacking on the other to the tail of the computation
            
            idx1val = idx1 == nullptr ? 0 : idx1->val;
            idx2val = idx2 == nullptr ? 0 : idx2->val;

            sum = idx1val + idx2val + carry;
            if (sum>9) {
                sum = sum-10;
                carry = 1;
            } else {
                carry = 0;
            }
            if (idx1!=nullptr)
                idx1->val = sum;
            else {
                // idx1 has run run, now use idx2's nodes
                assert (idx2 != nullptr);
                tail_of_result->next = idx2;
                //tail_of_result = tail_of_result->next;
                tail_of_result->next->val = sum;
            }
            if (tail_of_result->next != nullptr)
                tail_of_result = tail_of_result->next;
            if (idx1 != nullptr)
                idx1 = idx1->next;
            if (idx2 != nullptr)
                idx2 = idx2->next;
            if (idx1 == nullptr && idx2 == nullptr)
                break;
        }
        if (carry==1) {
            auto last = new ListNode;
            last->val = 1;
            last->next = nullptr;
            tail_of_result->next = last;
        }
        return res;
    }
};
