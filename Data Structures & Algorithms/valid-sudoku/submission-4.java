class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Integer>[] rows = new HashSet[9];
        Set<Integer>[] cols = new HashSet[9];
        Set<Integer>[][] boxes = new HashSet[3][3];

        for(int r=0;r<board.length;r++){
            rows[r] = new HashSet<>();
        }

        for(int c=0;c<board.length;c++){
            cols[c] = new HashSet<>();
        }

        for(int r=0;r<3;r++){
            for(int c=0;c<3;c++){
                boxes[r][c] = new HashSet<>();
            }
        }


        for(int r=0;r<board.length;r++){
            for(int c=0;c<board.length;c++){
                if (board[r][c] == '.') continue;

                int num = Integer.valueOf(board[r][c]);

                if (rows[r].contains(num)) return false;
                rows[r].add(num);

                if (cols[c].contains(num)) return false;
                cols[c].add(num);

                if (boxes[r/3][c/3].contains(num)) return false;
                boxes[r/3][c/3].add(num);
            }
        }
        return true;
    }
}
