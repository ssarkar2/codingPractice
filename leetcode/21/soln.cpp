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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        if (list1 == nullptr)
            return list2;
        if (list2 == nullptr)
            return list1;
        
        ListNode* retlist{list1->val < list2->val ? list1 : list2};
        ListNode* retlist_end{retlist};
        if (list1->val < list2->val) {
            list1 = list1->next;
        } else {
            list2 = list2->next;
        }
        retlist_end->next = nullptr;
        ListNode* tmp{nullptr};
        while((list1 != nullptr) && (list2 != nullptr)) {


            retlist_end->next = list1->val < list2->val ? list1 : list2;
            if (list1->val < list2->val) {
                list1 = list1->next;
            } else {
                list2 = list2->next;
            }
            retlist_end->next->next  = nullptr;
            retlist_end = retlist_end->next;
        }

        if (list1 == nullptr) {
            retlist_end->next = list2;
        } else {
            retlist_end->next = list1;
        }
        return retlist;
    }
};
