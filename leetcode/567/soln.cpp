class Solution {
public:

    std::unordered_map<char, int> hist(const string& s1) {
        std::unordered_map<char, int> result;
        for (auto i : s1) {
            auto iter = result.find(i);
            if (iter == result.end()) {
                result.insert({i, 1});
            } else {
                iter->second += 1;
            }
        }
        return result;
    }
    bool checkInclusion(string s1, string s2) {
        // create hist of s1
        // start with a window of len(s1) on s2, create its hist.
        // shift window, kick out leftmost, add rightmost
        // recompare with hist of s1
        if (s2.size() < s1.size())
            return false;
        auto refhist = hist(s1);
        auto windowhist = hist(s2.substr(0, s1.size()));
        if (refhist == windowhist)
            return true;
        for (int i = 1; i <= s2.size() - s1.size(); i++) {
            // update windowhist
            auto left = s2[i-1];
            auto right = s2[i+s1.size()-1];
            if (left != right) {
                auto left_iter = windowhist.find(left);
                if (left_iter->second > 1) {
                    left_iter->second -= 1;
                } else {
                    windowhist.erase(left_iter);
                }
                auto right_iter = windowhist.find(right);                
                if (right_iter == windowhist.end()) {
                    // add new entry
                    windowhist.insert({right, 1});
                } else {
                    right_iter->second += 1;
                }
            }
            if (refhist == windowhist)
                return true;
        }
        return false;
    }
};
