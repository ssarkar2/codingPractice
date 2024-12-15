class Solution {
public:
    void sortColors(vector<int>& nums) {
        uint r = 0, w = 0, b = 0;
        for (auto& i : nums) {
            if (i == 0) {
                r++;
            } else if (i == 1) {
                w++;
            } else {
                b++;
            }
        }
        for (uint i = 0; i < nums.size(); i++) {
            if (r > 0) {
                nums[i] = 0;
                r--;
            } else if (w > 0) {
                nums[i] = 1;
                w--;
            } else {
                nums[i] = 2;
            }
        }
    }
};
