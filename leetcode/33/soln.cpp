class Solution {
public:

    // -1: pivot on left, +1, pivot on right, 0 means on pivot
    int detectPivotLoc(vector<int>& nums, uint idx, uint left, uint right) {
        // assert idx in range
        if (idx == 0) {
            return 0;
        } else {
            // because nums are unique, its strict monotonic, no need to check for ==
            // bool notPivot = (nums[idx-1] < nums[idx]) && (nums[idx] < nums[idx+1]);
            if ((nums[idx] < nums[left]) && (nums[idx] < nums[right])) {
                return -1;
            } else if ((nums[idx] > nums[left]) && (nums[idx] > nums[right])) {
                return 1;
            } else {
                // assert left < mid, mid > right
                return 0;
            }
        }
    }

    int regularBinSearch(vector<int>& nums, int target, uint left, uint right) {
        if (nums[left] == target)
            return left;
        if (nums[right] == target)
            return right;
        uint prevmid = 0;
        int valmid;
        uint mid;
        while(true) {
            mid = (left + right) / 2;
            valmid = nums[mid];
            if (valmid == target) {
                return mid;
            }
            if (prevmid == mid) { // cases such as [1,3], target=0
                return -1;
            } else{
                prevmid = mid;
            }
            if (target < valmid) {
                right = mid;
            } else {
                left = mid;
            }
        }
    }


    int search(vector<int>& nums, int target) {
        uint left = 0;
        uint right = nums.size() - 1;
        // check if elem is in 0 or last posn
        // check if unrotated
        int valmid, pivotLocation;
        uint mid;
        bool noPivot = false;
        //establish an invariant that left and right will never contain the target
        if (nums[left] == target)
            return left;
        if (nums[right] == target)
            return right;
        uint prevmid = 0;
        while(true) {
            //printf("----%d %d %b\n", left, right, noPivot);
            if (left == right) {
                return nums[left] == target ? left : -1;
            }
            if (!noPivot){
                noPivot = nums[left] < nums[right];
                //printf("not free of pivot=%d\n", noPivot);
            }
            mid = (left + right) / 2;
            valmid = nums[mid];
            if (valmid == target) {
                return mid;
            }
            if (prevmid == mid) { // cases such as [1,3], target=0
                return -1;
            } else{
                prevmid = mid;
            }
            if (noPivot) {
                return regularBinSearch(nums, target, left, right);
            } else {
                pivotLocation = detectPivotLoc(nums, mid, left, right);
                if (pivotLocation==1) {
                    if ((target < valmid) && (target > nums[left])) {
                        right = mid; 
                    } else {
                        left = mid;
                    }
                } else if (pivotLocation==-1) {
                    if ((target > valmid) && (target < nums[right])) {
                        left = mid;
                    } else {
                        right = mid;
                    }
                } else {
                    //sitting on the pivot
                    if (target > nums[left] && target > nums[right]) {
                        right = mid; // add an assert that next round noPivot should flip to true
                    } else {
                        left = mid;
                    }
                }
            }
        }
    }
};
