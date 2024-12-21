class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        sort(nums.begin(), nums.end());
        int max_run = 0;
        int curr_run = 1;
        for (int i = 1; i < nums.size(); i++) {
            if ((nums[i] - nums[i-1] == 1) || (nums[i] == nums[i-1])) {
                if (nums[i] > nums[i-1])
                    curr_run++;
            } else {
                if (curr_run > max_run)
                    max_run = curr_run;
                curr_run = 1;
            }
        }
        if (curr_run > max_run)
            max_run = curr_run;
        return max_run;
    }
};
