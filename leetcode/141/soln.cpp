/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:

    bool hasCycle(ListNode *head) {
    if (head == nullptr)
        return false;
    auto fast = head->next;
    auto slow = head;
    while(true) {
        if (fast == nullptr || fast->next == nullptr) {
            return false;
        } else {
            if (fast == slow || fast->next == slow) {
                return true;
            }  else {
                fast = fast->next->next;
                slow = slow->next;
            }
        }
    }
}
