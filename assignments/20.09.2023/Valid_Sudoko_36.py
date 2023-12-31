class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]  # To store numbers seen in each row.
        cols = [set() for _ in range(9)]  # To store numbers seen in each column.
        boxes = [set() for _ in range(9)]  # To store numbers seen in each 3x3 sub-box.

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                # Check row.
                if num in rows[i]:
                    return False
                rows[i].add(num)

                # Check column.
                if num in cols[j]:
                    return False
                cols[j].add(num)

                # Check sub-box.
                box_idx = (i // 3) * 3 + (j // 3)
                if num in boxes[box_idx]:
                    return False
                boxes[box_idx].add(num)

        return True
