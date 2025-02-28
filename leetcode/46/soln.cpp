class Solution {
public:
    vector<vector<int>> helper(vector<int> state, vector<int> left_to_use) {
        if (left_to_use.size() == 0) {
            return {state};
        }
        vector<vector<int>> res;
        for (auto i : left_to_use) {
            vector<int> left_to_use_new;
            for(auto j : left_to_use) {
                if (j!=i)
                    left_to_use_new.push_back(j);
            }
            vector<int> state_new{state};
            state_new.push_back(i);
            auto x = helper(state_new, left_to_use_new);
            for (auto elem : x)
                res.push_back(elem);
        }
        return res;
    }

    vector<vector<int>> permute(vector<int>& nums) {
        return helper({}, nums);
    }
};
