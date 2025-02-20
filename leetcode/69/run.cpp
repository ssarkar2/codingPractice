class Solution {
public:
    int mySqrt(int n) {
        if (n==1)
            return 1;
        long int left = 0, right = n, mid = 0;
        while(left <= right) {
            mid = (left+right)/2;
            if (mid*mid <= n && (mid+1)*(mid+1) > n) {
                return mid;
            } else if (mid*mid <= n) {
                left = mid+1;
            } else {
                right = mid-1;
            }
        }
        return 0;
    }
};
