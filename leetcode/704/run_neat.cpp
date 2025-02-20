class Solution {
public:
    int search(vector<int>& data, int target) {
    int left = 0;
    int right = data.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (data[mid] == target) {
            return mid;
        } else if (data[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;

    }
};
