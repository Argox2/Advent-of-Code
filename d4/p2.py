def find_word_in_grid(grid, word):
    
    # row, col
    directions = [
        (0, 1),   # Right
        (1, 1),   # Down-Right
        (1, 0),   # Down
        (1, -1),  # Down-Left
        (0, -1),  # Left
        (-1, -1), # Up-Left
        (-1, 0),  # Up
        (-1, 1)   # Up-Right
    ]

    coordenates = [
        (-1, -1),
        (-1, 1), 
        (1, -1), 
        (1, 1)
    ]

    num_cols = len(grid[0])
    num_rows = len(grid)
    word_len = len(word)

    word_appears = 0


    def check_X(row, col, pivot):
        if grid[row + pivot[0]][col + pivot[1]] == word[0] and grid[row - pivot[0]][col - pivot[1]] == word[2] and grid[row + pivot[0]][col - pivot[1]] == word[0] and grid[row - pivot[0]][col + pivot[1]] == word[2]:
            return True

        if grid[row + pivot[0]][col + pivot[1]] == word[0] and grid[row - pivot[0]][col - pivot[1]] == word[2] and grid[row - pivot[0]][col + pivot[1]] == word[0] and grid[row + pivot[0]][col - pivot[1]] == word[2]:
            return True

        return False


    for row in range(num_rows):
        for col in range(num_cols):
            if (grid[row][col] == word[1]) and (0 < row < num_rows - 1) and (0 < col < num_cols - 1): # Find an A. 
                for pivot in coordenates:
                    if check_X(row, col, pivot):
                        word_appears += 1
                        break

    return(word_appears)

data = '''
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''.strip()

grid = [list(line) for line in data.split('\n')]
print(grid)

word = "MAS"

ocurrences = find_word_in_grid(grid, word)
print(ocurrences)


