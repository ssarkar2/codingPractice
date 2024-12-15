#include <stack>


class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        uint popIdx = 0, pushIdx=0;
        uint len = pushed.size();
        stack<int> stack;
        while(true) {
            if ((stack.size() >= 1) && (stack.top() == popped[popIdx])) {
                popIdx++;
                stack.pop();
                if (stack.size() == 0 && pushIdx >= (len-1))
                    return true; 
                continue;
            }
            
            if (pushIdx < len) {
                stack.push(pushed[pushIdx]);
                pushIdx++;
                continue;
            } else {
                return false;
            }
        }
    }
};
