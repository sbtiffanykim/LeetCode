class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        for (int x = 0; x < board.size(); x++) {
            for (int y = 0; y < board[0].size(); y++) {
                if (dfs(x, y, 0, word, board)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    bool dfs(int x, int y, int depth, string word, vector<vector<char>>& board) {
        if (depth == word.size()) return true;
        if (x < 0 || y < 0 || x >= board.size() || y >= board[0].size() || board[x][y] != word[depth] || board[x][y] == '#') return false;
        
        board[x][y] = '#';  // Mark as visited
        bool res = dfs(x+1, y, depth+1, word, board) || dfs(x-1, y, depth+1, word, board) || dfs(x, y+1, depth+1, word, board) || dfs(x, y-1, depth+1, word, board);
        board[x][y] = word[depth];
        return res;
    }
};