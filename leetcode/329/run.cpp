class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {

        int rows = matrix.size();
        int cols = matrix.at(0).size();
        vector<vector<int>> solutions(rows);
        for (int i = 0; i < rows; ++i) {
            solutions[i].resize(cols, -1);
        }

        auto get_neighbors = [rows, cols](int r, int c){
            vector<pair<int, int>> neighbors;
            for (auto [delr, delc] : vector<pair<int, int>>{{0,1}, {0,-1}, {1,0}, {-1,0}}) {
                if ((r+delr) >= 0 && (c+delc) >= 0 && (r+delr) < rows && (c+delc) < cols) {
                    neighbors.push_back({r+delr, c+delc});
                }
            }
            return neighbors;
        };

        // no reason to make this a lambda. was just checking how to make lambdas recursive (std::function (no auto), and capture name)
        // update solutions
        std::function<void(int, int)> get_best_path = [&get_best_path, &solutions, &matrix, &get_neighbors](int r, int c) {
            int currval = 0, best_neighbor_path_len = 0, nval = 0, neighbor_soln = 0;
            currval = matrix[r][c];
            best_neighbor_path_len = 0;
            for (auto [nr,nc] : get_neighbors(r, c)) {
                nval = matrix[nr][nc];
                if (nval <= currval) // >= ?. cannot use this neighbor to construct my long path
                    continue;
                if (solutions[nr][nc] == -1) { // answer hasn't been calculated already, so reuse
                    // calculate neighbor
                    get_best_path(nr, nc);
                }
                neighbor_soln = solutions[nr][nc];
                if (best_neighbor_path_len < 1+neighbor_soln){
                    best_neighbor_path_len = 1+neighbor_soln;
                }
            }
            solutions[r][c] = best_neighbor_path_len;
        };

        /*
        soln:
        -1 means: not calculated yet
        0 means, no path, ie matrix[i][j] is smaller than all its neighbors
        */
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (solutions[r][c] == -1) { // this position hasn't been solved already
                    get_best_path(r, c);
                }
                // assert solution[r][c] > -1
            }
        }

        // can i track the best when calc is happening, so avoid this O(r*c) pass at the end?
        int best_solution = 0;
        for(auto r : solutions) {
            for (auto c : r) {
                if (c > best_solution)
                    best_solution = c;
            }
        }

        return best_solution+1;
    }
};
// 37
