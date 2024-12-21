class Solution {
public:
    std::unordered_map<char, int> histogram(string s) {
        std::unordered_map<char, int> smap;
        for(char& c : s) {
            auto itr = smap.find(c);
            if (itr==smap.end()) {
                smap[c] = 1;
            } else {
                itr->second += 1;
            }
        }
        return smap;
    }
    bool isAnagram(string s, string t) {
        return histogram(s) == histogram(t);
    }
};
