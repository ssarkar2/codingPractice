class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        if (intervals.size() == 0) {
            return {newInterval};
        }
        vector<vector<int>> result;
        
        if (newInterval[0] <= intervals[0][0]) {
            if (newInterval[1] >= intervals[0][0])
                intervals[0][0] = newInterval[0];
            else {
                intervals.insert(intervals.begin(), newInterval);
                return intervals;
            }
        }
        
        int cnt = 0;

        while(true) {
            if (cnt < intervals.size() && intervals[cnt][1] < newInterval[0]) {
                result.push_back(intervals[cnt]);
                cnt++;
            } else
                break;
        }

        vector<int> merge_interval{cnt < intervals.size() ? min(intervals[cnt][0], newInterval[0]) : newInterval[0], newInterval[1]};
        while(true) {
            if (cnt < intervals.size() && intervals[cnt][1] <= newInterval[1]) {
                cnt++;
                continue;
            }
            if (cnt < intervals.size() && intervals[cnt][0] <= newInterval[1])
                merge_interval[1] = max(intervals[cnt][1], newInterval[1]);
                //cnt++;
            break;
        }
        result.push_back(merge_interval);
        while(cnt < intervals.size()) {
            if (intervals[cnt][0] > newInterval[1])
                result.push_back(intervals[cnt]);
            cnt++;
        }
        return result;
    }
};
