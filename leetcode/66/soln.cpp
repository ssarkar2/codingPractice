class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        auto idx = digits.rbegin();
        while(true) {
            if (idx == digits.rend())
                break;
            auto val = *idx;
            if (val == 9){
                *idx = 0;
                idx++;
            } else {
                *idx += 1;
                break;
            }
        }
        if (idx == digits.rend()) {
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
