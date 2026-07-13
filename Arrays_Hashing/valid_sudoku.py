from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subs = [set() for _ in range(9)]
        for i in range(0, 9):
            for j in range(0, 9):
                val = board[i][j]
                print(val)
                if val == ".":
                    continue
                if val in rows[i]:
                    print(val, i)
                    return False
                rows[i].add(val)
                if val in cols[j]:
                    print(val, j)
                    return False
                cols[j].add(val)
                idx = (i // 3) * 3 + (j // 3)
                if val in subs[idx]:
                    print(val, idx, i, j)
                    return False
                subs[idx].add(val)
        return True


board = [
    ["1", ".", "3", ".", ".", ".", ".", ".", "6"],
    ["2", ".", "5", ".", ".", ".", ".", ".", "7"],
    ["9", ".", "4", ".", ".", ".", ".", ".", "8"],
    ["6", ".", "7", ".", ".", ".", ".", ".", "2"],
    [".", "7", "8", ".", ".", ".", ".", ".", "1"],
    ["8", "2", "9", ".", ".", ".", ".", ".", "3"],
    [".", "8", "6", ".", ".", ".", ".", ".", "4"],
    ["7", "3", "2", ".", ".", ".", ".", ".", "5"],
    ["4", "5", "1", ".", ".", ".", ".", ".", "9"],
]

sol = Solution()
print(sol.isValidSudoku(board))
