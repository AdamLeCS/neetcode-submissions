class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = set() # set of nums 1-9
        # first check all rows
        for i in range(9):
            for j in range(9):
                curr_num = board[i][j]
                if (curr_num == "."):
                    continue
                elif curr_num not in nums:
                    nums.add(curr_num)
                else:
                    return False
            nums.clear()

        # check all columns
        nums.clear()
        for i in range(9):
            for j in range(9):
                curr_num = board[j][i]
                if (curr_num == "."):
                    continue
                elif curr_num not in nums:
                    nums.add(curr_num)
                else:
                    return False
            nums.clear()

        # check each grid of 9
        nums.clear()
        x_off = 0
        y_off = 0
        for j in range(3): # goes across the board
            for k in range(3): # goes down the board
                for l in range(3): # goes across the square
                    for m in range(3): # goes down the square
                        curr_num = board[l+3*k][m+3*j]
                        if (curr_num == "."):
                            continue
                        elif curr_num not in nums:
                            nums.add(curr_num)
                        else:
                            return False
                nums.clear()

        return True
        