__author__ = 'Local User'
# Sudoku Solver Project
'''
      ******************************************************
    DO NOT CHANGE THIS FUNCTION!

    It is provided for your convenience to be used in the
	is_possible_number() function.
    ******************************************************
'''
def get_cell_block(row,col) :
    block_row = row / 3
    block_col = col / 3
    block = block_row*3 + block_col
    return block

def is_possible_row(sudoku, row, number):
    # This is_possible_row() function returns true if the 'number'
    # argument is NOT already in the row of the 'sudoku' indexed
    # by the 'row' argument . This would mean that adding the
    # 'number' to the 'row' for this 'sudoku' is a potentially legal move.
    # (The 'sudoku' argument is a 9x9 two-dimensional array.)
    # This function should return false if the number already exists in
    # the specified row.
    "REPLACE THIS CODE WITH YOUR is_possible_row() METHOD"

def is_possible_column(sudoku, col, number) :
    # This is a lot like is_possible_row() above: it returns true if the 'number'
    # argument is NOT already in the column of the 'sudoku' indexed
    # by the 'col' argument . This would mean that adding the
    # 'number' to the 'col' for this 'sudoku' is a potentially legal move.
    # This function should return false if the number already exists in
    # the specified column.
    "REPLACE THIS CODE WITH YOUR is_possible_column() METHOD"

def is_possible_block(sudoku, block, number) :
    # A 'block' is a 3x3 area of the 'sudoku' in which numbers 1 to 9
    # must all be present. There are 9 of these zones in the Sudoku.
    # This method will return true if the 'number' argument is not already
    # in the block of the 'sudoku' specified by the 'block' argument --
    # again indicating a potentially legal move. (The 'sudoku' argument is,
    # as always, a 9x9 two-dimensional array.)
    # This method should return false if the 'number' already exists in the
    # specified 'block'.
    # The blocks are indexed from 0 to 8. The top row blocks being 0 to 2,
    # the middle row blocks being from 3 to 5 and the bottom row being 6 to 8.
    # Btw, the get_cell_block() function below might be helpful here.
    " REPLACE THIS CODE WITH YOUR is_possible_block() METHOD"

def is_possible_number(sudoku, row, col, number) :
    # Now you will start using of the other methods you've written above.
    # This method accepts a 'sudoku' puzzle, a 'row' and a 'col' (column), and a
    # possible 'number' to move into that row/column position.
    # Such a move would be possible if: 1) is_possible_row() returns true for
    # that row, and 2) ifPossibleColumn() returns true for that column, and
    # 3) is_possible_block() returns true for the block that sudoku[row][col] is
    # in. Use the get_cell_block() function below to find which block this is. If all of
    # these functions return true, then is_possible_number() should return true.
    # If any of the those functions returns false, then ifPossibleNumber() should
    # return false.
    "REPLACE THIS CODE WITH YOUR is_possible_number() METHOD"

def is_correct_row(sudoku, row) :
    # This method should return true if all the numbers from 1 to 9 are
    # present in the row indexed by the 'row' argument in the 'sudoku'
    # puzzle. It should return false if the row is incomplete or has duplicates.
    # Note that the "empty" rows will actually contain the value 0.
    # 1) Start off by making a *copy* of the row.
    # 2) Then sort the new array that you have made so that the
    # numbers run in ascending order.
    # 3) You should then be able to run through this sorted array and
    # easily determine if all the required numbers are there.
    "REPLACE THIS CODE WITH YOUR is_correct_row() METHOD"

def is_correct_column(sudoku, col) :
    # This method should return true if all the numbers from 1 to 9
    # are present in the column indexed by the 'col' argument in the
    # 'sudoku' puzzle. It should return false if the column is incomplete
    # or has duplicates.
    # This method is analogous to the is_correct_row() method above.
    " REPLACE THIS CODE WITH YOUR is_correct_column() METHOD"

def is_correct_block(sudoku, block) :
    # This function is very similar to the previous two above except
    # that you will again have to figure out how to index all the elements
    # in the 'sudoku' array for the block specified by the 'block' argument.
    # This function should return true if all the numbers from 1 to 9 are
    # in the block. It should return false if the block is incomplete or
    # contains duplicates.
    "REPLACE THIS CODE WITH YOUR is_correct_block() METHOD"

def is_solved(sudoku) :
    # A sudoku will be solved if all its rows, columns and blocks are correct.
    # Use a combination of the previous three functions -- is_correct_row(),
    # is_correct_column(), and is_correct_block() -- to determine if the 'sudoku'
    # is solved and return true if this is the case. If the sudoku is not solved,
    # you should return false.
    "REPLACE THIS CODE WITH YOUR is_solved() METHOD"