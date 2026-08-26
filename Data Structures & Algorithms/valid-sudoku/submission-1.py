class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #main part is to make 3 sets(does not contain duplicates)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set)

        #now iterate over the two by two matrix, add unseen elements in the set and if they are seen again row and column wise then return false else return true at the end. Double for loop

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in box[(r // 3, c // 3)]:
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    box[(r // 3, c // 3)].add(board[r][c])
        return True