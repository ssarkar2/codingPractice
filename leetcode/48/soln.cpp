class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // ith row becomes nc-i th col
        int n = matrix.size();
        int tmp0, tmp1, tmp2;
        for (int shell_id = 0; shell_id  < (n/2) ; shell_id++) {
            // in outermost shell there are n elems, next one has n-2.
            // so for shell i, need to rotate n-2*shell_id elems
            for (int i = 0; i < n-2*shell_id-1; i++) {
                // rotate 4 elems here
                // when in shell_id, we are operating on:
                // rows = shell_id, n-1-shell_id
                // cols = shell_id, n-1-shell_id
                // the 4 items swapping are:
                // (shell_id, shell_id+i), (shell_id+i, n-1-shell_id), (n-1-shell_id, n-1-i-shell_id), (n-1-i-shell_id, shell_id)
                tmp0 = matrix[shell_id+i][n-1-shell_id];
                tmp1 = matrix[n-1-shell_id][n-1-i-shell_id];
                tmp2 = matrix[n-1-i-shell_id][shell_id];
                matrix[shell_id+i][n-1-shell_id] = matrix[shell_id][shell_id+i];
                matrix[n-1-shell_id][n-1-i-shell_id] = tmp0;
                matrix[n-1-i-shell_id][shell_id] = tmp1;
                matrix[shell_id][shell_id+i] = tmp2;
            }
        }
    }
};
