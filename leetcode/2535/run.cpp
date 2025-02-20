#include<algorithm>
#include <functional>
#include <iostream>
#include <numeric>

void sum_digits(int &n) {
    int sum = 0;
    while(true) {
        sum += (n%10);
        n /= 10;
        if (n==0){
            n = sum;
            return;
        }
    }
}


int sum_digits1(int n) {
    int sum = 0;
    while(true) {
        sum += (n%10);
        n /= 10;
        if (n==0){
            return sum;
        }
    }
}

class Solution {
public:
    
    int differenceOfSum(vector<int>& nums) {

        /*
        int sum = std::accumulate(nums.cbegin(), nums.cend(), 0, std::plus<int>{});

        std::for_each(nums.begin(), nums.end(), std::function<void(int&)>(sum_digits));
        int sumdigs = std::accumulate(nums.cbegin(), nums.cend(), 0, std::plus<int>{});

        return std::abs(sum - sumdigs);
        */
        std::vector<int> nums_digitsadded;
        std::transform(nums.begin(), nums.end(), std::back_inserter(nums_digitsadded), std::function<int(int)>(sum_digits1));
        return std::inner_product(nums.begin(), nums.end(), nums_digitsadded.begin(), 0, std::plus<>(), std::minus<>());
    }

};
