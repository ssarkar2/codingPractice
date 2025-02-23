#include <ranges>

class Solution {
public:
    vector<string> helper(string state, int num_opens, int num_left_to_open) {
        vector<string> result;
        if (num_opens == 0 && num_left_to_open == 0) {
            return {state};
        }
        if (num_left_to_open > 0) {
            auto res_open = helper(state + "(", num_opens+1, num_left_to_open-1);
            result.insert(result.end(), res_open.begin(), res_open.end());
        }
        if (num_opens > 0){
            auto res_close = helper(state + ")", num_opens-1, num_left_to_open);
            result.insert(result.end(), res_close.begin(), res_close.end());
        }
        return result;
    }

    vector<string> generateParenthesis(int n) {
        return helper("", 0, n);
    }
};
