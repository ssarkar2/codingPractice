class Solution {
public:
    int search(vector<int>& arr, int target) {
        auto left = arr.cbegin();
        auto right = arr.cend();
        auto start_itr = arr.cbegin();
        int midval = 0;
        std::vector<int>::const_iterator mid;
        if (arr.size() == 0)
            return -1;
        while(true){
            std::cout << std::distance(arr.cbegin(), left) << "  " << std::distance(arr.cbegin(), right) << "\n";
            if (right <= left) {
                if (right < arr.cend() && right >= start_itr && *right == target)
                    return std::distance(arr.cbegin(), right);
                else if (left < arr.cend() && left >= start_itr && *left == target)
                    return std::distance(arr.cbegin(), left);
                else
                    return -1;
            }
            mid = start_itr + ((std::distance(start_itr, left) + std::distance(start_itr, right))/ 2);
            midval = *mid;
            if (midval == target) {
                return std::distance( arr.cbegin(), mid);
            } else if (midval < target) {
                left = mid+1;
            } else {
                right = mid-1;
            }
        }
        return 0;
    }
};
