class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /*
        sort(nums.begin(), nums.end());

        int start = 0, end = nums.size()-1;
        int currsum;
        while(true) {
            currsum = nums[start] + nums[end];
            printf("%d %d.. %d %d %d\n", start, end, currsum, nums[start], nums[end]);
            if (currsum == target) {
                return {start, end};
            } else if (currsum < target) {
                start++;
            } else {
                end--;
            }
            //if (start == end)
            //no need to worry about no soln case 
        }

        // need to convert the sorted index back to original order
        */

        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1; j < nums.size(); j++) {
                if (nums[i]+nums[j] == target) {
                    return {i,j};
                }
            }
        }
        return {-1,-1};
    }
};
