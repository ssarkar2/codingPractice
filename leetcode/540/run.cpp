class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {

        int sz = nums.size();
        // 0 : mid is the ans
        // -1 : mid is bad
        // 1 mid is good
        auto get_twin_state = [&nums, &sz](int idx) {
            auto left_neighbor = idx-1 >= 0 ? std::optional<int>(nums[idx-1]) :  std::nullopt;
            auto right_neighbor = idx-1 >= 0 ? std::optional<int>(nums[idx+1]) :  std::nullopt;

            auto expected_neighbour = idx%2 == 0 ? right_neighbor : left_neighbor;
            auto other_neighbour = idx%2 == 0 ? left_neighbor : right_neighbor;

            if (expected_neighbour && *expected_neighbour == nums[idx]) {
                return 1;
            } else {
                return (other_neighbour && (*other_neighbour == nums[idx])) ? -1 : 0;
            }
        };

        int left = 0, mid = 0, midval = -1;
        int right = nums.size();
        int state = 0;
        while(left <= right) {
            mid = (left + right)/2;
            midval = nums[mid];
            state = get_twin_state(mid);
            if (state == 0) {
                return midval;
            } else if (state==1) {
                left = mid+1;
            } else {
                right = mid-1;
            }
        }
        return nums[mid];
    }
};
