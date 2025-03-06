class Solution {
public:

    using Board = vector<string>;
    using Coord = pair<int, int>;

    void update_diagonal_attack_vectors(Board& board, int r, int c) {
        // mark all diagonals from r,c as 'A'
        int n = board.size();
        for (auto direction : vector<pair<int, int>>{{1,1}, {1,-1}, {-1,1}, {-1,-1}}) {
            auto [delr, delc] = direction;
            int newr = r;
            int newc = c;
            while(true) {
                newr += delr;
                newc += delc;
                if (newr >= 0 && newc >= 0 && newr < n && newc < n) {
                    //if (board[newr][newc] == '.')
                        board[newr][newc] = 'A';
                } else
                    break;
            }
        }
    }


    void print_board(Board board) {
        for (auto r : board) {
            cout << r << "\n";
        }
    }

    // num_queens_left = len(state_of_board) - len(queen_locs)
    vector<Board> helper(Board state_of_board, set<int> queen_rows, set<int> queen_cols) {
        int num_queens_placed = queen_rows.size();
        int n = state_of_board.size();
        if (num_queens_placed == n) {
            return {state_of_board};
        }
        vector<Board> result;
        for (int r = 0; r < n; r++) {
            if (queen_rows.find(r) != queen_rows.end())
                continue;
            bool found_success_for_this_row = false;
            for (int c = 0; c < n; c++) {
                if (queen_cols.find(c) != queen_cols.end())
                    continue;
                if (state_of_board[r][c] == '.') {
                    set<int> queen_rows_new(queen_rows);
                    set<int> queen_cols_new(queen_cols);
                    //assert (queen_rows_new.find(r) == queen_rows_new.end());
                    //assert (queen_cols_new.find(c) == queen_cols_new.end());
                    queen_rows_new.insert(r);
                    queen_cols_new.insert(c);
                    Board state_of_board_new(state_of_board);
                    state_of_board_new[r][c] = 'Q'; // place queen
                    update_diagonal_attack_vectors(state_of_board_new, r, c); // Add 'A'
                    //cout << "place queen at " << r << " " << c << "\n";
                    //print_board(state_of_board_new);
                    auto tmp = helper(state_of_board_new, queen_rows_new, queen_cols_new);
                    if (tmp.size() > 0) {
                        result.insert(result.end(), tmp.begin(), tmp.end());
                    }
                }
            }
            if (!found_success_for_this_row) // early exit criteria
                break;
        }
        //if (result.size() == 0)
        //    cout << "No Configs found\n";
        return result;
    }

    void cleanup(vector<Board>& all_results) {
        if (all_results.size() == 0)
            return;
        int n = all_results[0].size();
        for (auto& board : all_results) {
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    if (board[r][c] == 'A')
                        board[r][c] = '.';
                }
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        // create initial board
        // .: empty
        // A: under attack
        // Q: queen

        Board initial_board;
        for (int r = 0; r < n; r++) {
            //auto string tmp(n, '')
            initial_board.emplace_back(n, '.');
        }

        set<int> queen_rows, queen_cols;
        auto res = helper(initial_board, queen_rows, queen_cols);
        // clean up res, remove 'A'
        cleanup(res);
        return res;
    }
};

// 8 + 21 + 15 + 28
