#include <stack>
#include <unordered_set>

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {

        // DFS, stack
        using Coordinate = std::pair<int, int>;
        std::stack<Coordinate> stack;
        std::set<Coordinate> visited{};
        int rows = grid.size();
        int cols = grid.at(0).size();

        auto get_neighbors = [rows, cols, &grid](const Coordinate& coord){
            auto [r, c] = coord;
            std::vector<Coordinate> neighbors;
            for (auto [delr, delc] : std::vector<std::pair<int, int>> {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}){
                if (r+delr >= 0 && c+delc >=0 && r+delr < rows && c+delc < cols) { // valid location
                    if (grid.at(r+delr).at(c+delc) == 1) // has a "1"
                        neighbors.push_back(std::pair{r+delr, c+delc}); //CTAD works on pair
                }
            }
            return neighbors;
        };
        int count_area, max_area = 0;
        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++){
                if (grid.at(r).at(c) == 0)
                    continue;
                if (visited.find({r,c}) != visited.end())
                    continue;
                count_area = 0;
                stack.push({r,c});
                while(stack.size()!=0) {
                    auto curr_node = stack.top();
                    stack.pop();
                    if (visited.find(curr_node) == visited.end()){
                        visited.insert(curr_node);
                        count_area += 1;
                        auto neighbors = get_neighbors(curr_node);
                        for (const auto& n : neighbors) {
                            if (visited.find(n) == visited.end()) {
                                stack.push(n);
                            }
                        }
                    }
                }
                if (max_area < count_area){
                    max_area = count_area;
                }
            }
        }
        return max_area;
        
    }
};
// 63 min
