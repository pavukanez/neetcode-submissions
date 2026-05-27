class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int r=0;r<9;r++){
            Set<Character> seen = new HashSet<>();
            for(int c=0;c<9;c++){
                if (board[r][c] == '.') continue;
                if (seen.contains(board[r][c])) return false;
                seen.add(board[r][c]);
            }
        }

        for(int c=0;c<9;c++){
            Set<Character> seen = new HashSet<>();
            for(int r=0;r<9;r++){
                if (board[r][c] == '.') continue;
                if (seen.contains(board[r][c])) return false;
                seen.add(board[r][c]);
            }
        }

        Set<Character>[][] boxes = new HashSet<>[3][3];
        for(int r=0;r<9;r++){
            for(int c=0;c<9;c++){
                if (board[r][c] == '.') continue;

                if (boxes[r/3][c/3] == null) boxes[r/3][c/3] = new HashSet<>();
                if (boxes[r/3][c/3].contains(board[r][c])) return false;
                boxes[r/3][c/3].add(board[r][c]);
            }
        }

        return true;
    }
}
