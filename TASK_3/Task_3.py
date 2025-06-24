def print_sudoku(grid):
    """Prints the Sudoku grid in a readable format"""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()

def find_empty(grid):
    """Finds the next empty cell (0) in the grid"""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # row, column
    return None

def is_valid(grid, num, pos):
    """Checks if placing 'num' at position 'pos' is valid"""
    row, col = pos
    
    # Check row
    if num in grid[row]:
        return False
    
    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grid[i][j] == num and (i,j) != pos:
                return False
    
    return True

def solve_sudoku(grid):
    """Solves the Sudoku using backtracking"""
    empty = find_empty(grid)
    if not empty:
        return True  # Puzzle solved
    
    row, col = empty
    
    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            
            if solve_sudoku(grid):
                return True
            
            grid[row][col] = 0  # Backtrack if solution not found
    
    return False

def get_sudoku_input():
    """Gets Sudoku input from the user"""
    print("Enter your Sudoku puzzle (9 rows, 9 numbers each, 0 for empty cells):")
    grid = []
    for i in range(9):
        while True:
            row_str = input(f"Row {i+1}: ").strip()
            if len(row_str) != 9:
                print("Please enter exactly 9 digits (0-9)")
                continue
            try:
                row = [int(c) for c in row_str]
                if any(n < 0 or n > 9 for n in row):
                    print("Numbers must be between 0-9")
                    continue
                grid.append(row)
                break
            except ValueError:
                print("Please enter digits only (0-9)")
    return grid

# Example usage
if __name__ == "__main__":
    print("SUDOKU SOLVER")
    print("-------------")
    
    # Get input grid
    sudoku = get_sudoku_input()
    
    print("\nInput Sudoku:")
    print_sudoku(sudoku)
    
    # Solve the Sudoku
    if solve_sudoku(sudoku):
        print("\nSolved Sudoku:")
        print_sudoku(sudoku)
    else:
        print("\nNo solution exists for this Sudoku puzzle.")
