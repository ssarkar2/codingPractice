#include <unordered_set>


class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> helper;
        vector<int> result;
        for (auto& i : nums1)
            helper.insert(i);

        for (auto& i : nums2) {
            if (auto iter = helper.find(i); iter != helper.end()) {
                result.push_back(i);
                helper.erase(iter);
            }
        }
        return result;
    }
};
