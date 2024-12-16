class Solution {
public:

    bool noOverlap(vector<int>& nums1, vector<int>& nums2) {
        return (nums1.back() < nums2[0]) || (nums2.back() < nums1[0]);
    }

    //-1 means nums1 is bigger, +1 means nums2 is bigger, 0 means not a full overlap
    int fullOverlap(vector<int>& nums1, vector<int>& nums2) {
        if ((nums1[0] < nums2[0]) && (nums1.back() > nums2.back())) {
            return -1;
        } else if ((nums2[0] < nums1[0]) && (nums2.back() > nums1.back())) {
            return 1;
        } else {
            return 0;
        }

    }

    vector<int> removeRedundancies(vector<int>& nums) {
        if (nums.size() == 0) {
            return {}
        }
        vector<int> result;
        int lastUniqueItem = nums[0];
        result.push_back(lastUniqueItem);
        for (uint i=1 ; i<nums.size(); i++) {
            if (nums[i] == lastUniqueItem) {
                continue;
            } else {
                lastUniqueItem = nums[i];
                result.push_back(lastUniqueItem);
            }
        }
        return result;
    }

    vector<int> helper(vector<int>& nums1, vector<int>& nums2) {
        
    }

    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        auto comp = [](int a, int b){return a > b;};
        sort(nums1.begin(), nums1.end(), comp);
        sort(nums2.begin(), nums2.end(), comp);

        if (noOverlap(nums1, nums2)) {
            return {};
        }

        int fullOv = fullOverlap(nums1, nums2);
        if (fullOv == -1) {
            return removeRedundancies(nums2);
        } else if(fullOv == 1) {
            return removeRedundancies(nums1);
        } else {
            if (nums1[0] < nums2[0]) {
                return helper(nums1, nums2);
            } else {
                return helper(nums2, nums1);
            }
        }
    }
};
