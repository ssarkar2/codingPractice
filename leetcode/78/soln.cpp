class Solution {
public:

    vector<vector<int>> subsets(vector<int>& nums) {
        int num_elems = nums.size();
        bool bit = 0;
        vector<vector<int>> final;
        for (int i = 0; i < 1<<num_elems; i++) {
            vector<int> cur_set;
            for (int bitid = 0; bitid < num_elems; bitid++) {
                if ((i >> bitid) & 1)
                    cur_set.push_back(nums[bitid]);
            }
            final.push_back(cur_set);
        }
        return final;
    }
};
