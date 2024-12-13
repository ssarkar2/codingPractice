#include <vector>
#include <assert.h>
using namespace std;
class Solution {
    private:
    int get_unmarked_elem_idx(vector<int>& nums, const vector<bool>& marked) {
        int minval;
        long retidx = -1;
        bool minvalinitialized = false;
        for (int i = 0; i < nums.size(); i++) {
            if (!marked[i]) {
                if (minvalinitialized) {
                    if (nums[i] < minval) {
                        minval = nums[i];
                        retidx = i;
                    }
                } else {
                    minval = nums[i];
                    retidx = i;
                    minvalinitialized = true;
                }
            }
        }
        return minvalinitialized ? retidx : -1;
    }
public:
    long long findScore(vector<int>& nums) {
        long numlen = nums.size();
        vector<bool> marked(numlen, false);
        long idx;
        long long score = 0;
        while(true) {
            idx = get_unmarked_elem_idx(nums, marked);
            if (idx < 0)
                break;
            marked[idx] = true;
            if (idx-1 >= 0)
                marked[idx-1] = true;
            if (idx+1 <= numlen)
                marked[idx+1] = true;
            score += nums[idx];
        }
        return score;
    }
};


int main() {
    std::vector<int> nums = {2,1,3,4,5,2};
    assert(Solution().findScore(nums) == 7);
    std::vector<int> nums1 = {2,3,5,1,3,2};
    assert(Solution().findScore(nums1) == 5);
}


