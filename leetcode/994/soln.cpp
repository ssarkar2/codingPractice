class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        
        int rows = grid.size();
        int cols = grid[0].size();
        using Coord = pair<int, int>;

        auto get_fresh_neighbors = [&rows, &cols, &grid](int r, int c){
            //assert (grid[r][c] == 1 || grid[r][c] == 2); // remove later
            vector<Coord> res;
            for (auto [delr, delc] : vector<Coord>{{-1,0}, {1,0}, {0,-1}, {0,1}}) {
                if (delr+r >= 0 && delr+r < rows && delc+c >= 0 && delc+c < cols && grid[delr+r][delc+c] == 1)
                    res.push_back({delr+r, delc+c});
            }
            return res;
        };

        
        queue<Coord> q;
        // collect initial rotten oranges
        int num_fresh = 0;
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) {
                    //cout << "inserting " << r << " " << c << "\n";
                    q.push({r, c});
                }
                if (grid[r][c] == 1){
                    num_fresh++;
                }
            }

        
        int num_elems_in_level = 0;
        int mins = 0;
        //set<Coords> visited; //  could use grid[r][c] = 3 to indicate "visited"
        bool level_start = false;
        while(q.size() > 0) {
            if (num_elems_in_level == 0) {
                num_elems_in_level = q.size();
                // mins++; // cant increment mins here at start of new level. must wait till atleast 1 valid neighbor is added to next level
                level_start = true;
                //cout << "level start\n";
            }
            auto [r, c] = q.front();
            //cout << "processing " << r << " " << c << "\n";
            if (grid[r][c] == 3) {
                q.pop();
                continue;
            }
            for (auto [nr, nc] : get_fresh_neighbors(r, c)) {
                //if (visited.find({nr,nc}) != visited.end())
                if (grid[nr][nc] == 3)
                    continue;
                //assert (grid[nr][nc] == 1);
                grid[nr][nc] = 2;
                num_fresh--;
                q.push({nr,nc});
                if (level_start) {
                    mins++;
                    level_start = false;
                }
            }
            if (level_start && grid[r][c] == 1) {
                mins++;
                level_start = false;
            }
            grid[r][c] = 3; // mark visited (is rotten, and neighbors have been added to q)
            q.pop();
            num_elems_in_level--;
        }
        
        bool found_fresh = num_fresh!=0;
        /*for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    found_fresh = true;
                    break;
                }
            }
            if (found_fresh)
                break;
        }*/
        return found_fresh ? -1 : mins;
    }
};
