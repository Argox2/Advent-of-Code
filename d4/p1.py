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

    num_cols = len(grid[0])
    num_rows = len(grid)
    word_len = len(word)

    word_appears = 0


    def is_valid(cur_row, cur_col):
        return ((0 <= cur_row < num_rows) and (0 <= cur_col < num_cols))


    def check_dir(row, col, direction):
        for k in range(1, word_len):

            cur_row = row + (direction[0] * k)
            cur_col = col + (direction[1] * k)

            if not is_valid(cur_row, cur_col):
                return False
            if grid[cur_row][cur_col] != word[k]:
                return False

        return True


    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == word[0]:
                for direction in directions:
                    if check_dir(row, col, direction):
                        word_appears += 1

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

word = "XMAS"

ocurrences = find_word_in_grid(grid, word)
print(ocurrences)


