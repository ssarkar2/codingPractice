#include <set>

class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        uint budget = candyType.size() / 2;
        std::set<int> a;
        for (auto& k : candyType) {
            a.insert(k);
        }
        return a.size() > budget ? budget : a.size();
    }
};
