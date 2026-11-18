def make_grid(num_rows, num_columns):
    """
    A function to take in a grid of "#" and "-"
    ("#" represents a mine
    "-" represents a mine-free spot)

    Parameters:
    num_rows (int):The number of rows in the grid.

    num_columns (int): The number of columns in each row.

    Returns:
    empty_grid: The grid containing # and -
    """

    # Arrange the data input into an empty grid, stored in variable empty_grid 
    empty_grid = [[None] * num_columns for i in range(num_rows)]
    # print(empty_grid)

    # Assign values to elements in the list by looping through each row, then each column

    for row_index in range(num_rows):
        print(f"Assign either # or - to each column in row {row_index + 1}:")
        for col_index in range(num_columns):
            while True:
                col = input("Please enter # or - : ")
                if col not in {"#", "-"}:
                    print("Invalid input.")
                    continue
                break
            empty_grid[row_index][col_index] = col

    return empty_grid


def check_for_mines(grid, row, col):
    """
    A function that checks, for a given cell, how many mines (#) are adjacent to it and returns that number.
    """
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] == "#":
                count += 1
    return count


full_grid = make_grid(3, 3)

for r, row in enumerate(full_grid):
    for c, col in enumerate(full_grid[0]):
        if col == "-":
            full_grid = check_for_mines(full_grid, r, c)

print(full_grid)
