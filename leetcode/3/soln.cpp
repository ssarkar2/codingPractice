class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // keep an idx for current "front"
        // it time "i" we are trying to decide if s[i] can successfully extend the run
        // a map: locmap = char->idx
        // if s[i] in locmap:
        //    update front to locmap[s[i]]+1
        // else:
        //    ... successful extension. add to locmap

        // remember to track the max
        if (s.size() == 0)
            return 0;
        

        map<char, int> locmap; // set would be fine here.. we dont really need the "values", just the keys are enough
        int front = 0, newfront = 0;
        locmap.insert({s[0], 0});
        int maxsize = 1;
        char currchar;
        int currlen = 1;
        for (int i = 1; i < s.size(); i++) {
            currchar = s.at(i);
            auto itr = locmap.find(currchar);
            if (itr == locmap.end()) {
                // successful extension
                currlen++;
            } else {
                //need to pop
                newfront = itr->second+1;
                auto x = itr->second;
                for (int j = front; j <= x; j++) {
                    locmap.erase(s.at(j));
                }
                front = newfront;
                currlen = (i-front+1);
            }
            locmap.insert({currchar, i});
            if (currlen > maxsize)
                maxsize = currlen;
        }
        return maxsize;
    }
};
