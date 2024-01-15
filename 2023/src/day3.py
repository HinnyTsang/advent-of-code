from pathlib import Path

day = "day3"
puzzle_path = Path("puzzle")


with open(puzzle_path / f"{day}.txt", "r", encoding="utf-8") as puzzle:
    number_matrix = [row.strip() for row in puzzle.readlines()]

    def try_get(i: int, j: int):
        try:
            return number_matrix[i][j]
        except IndexError:
            return None

    def adj_symbol(value: int, x: int, col_start: int, col_end: int) -> bool:
        dxs = [0, 1, 1, 1, 0, -1, -1, -1]
        dys = [-1, -1, 0, 1, 1, 1, 0, -1]

        for y in range(col_start, col_end):
            for dx, dy in zip(dxs, dys):
                val = try_get(x + dx, y + dy)
                if val and not val.isdigit() and val != ".":
                    return True
        return False

    result = 0
    for i, row in enumerate(number_matrix):
        j, n = 0, len(row)
        while j < n:
            j_cache = j
            value = 0
            while j < n and row[j].isdigit():
                value = value * 10 + int(row[j])
                j += 1
            if value and adj_symbol(value, i, j_cache, j):
                result += value
            j += 1

    print(result)

# Part 2
with open(puzzle_path / f"{DAY}.txt", "r", encoding="utf-8") as puzzle:
    number_matrix = [row.strip() for row in puzzle.readlines()]

    class Null(str):
        def isdigit(self) -> bool:
            return False
    def try_get(i: int, j: int):
        try:
            return number_matrix[i][j]
        except IndexError:
            return Null()

    idx_of_star = [(i, j) for i, row in enumerate(number_matrix) for j, val in enumerate(row) if val == "*"]

    # Definition of two number
    def count_number(i, j):
        # First row
        def count_number_in_row(i, j):
            is_digits = [try_get(i, j + k).isdigit() for k in range(3)]
            match is_digits:
                case [False, False, False]:
                    return 0
                case [True, False, True]:
                    return 2
                case _:
                    return 1
        return sum([
            count_number_in_row(i - 1, j),
            count_number_in_row(i + 1, j),
            1 if try_get(i, j - 1).isdigit() else 0,
            1 if try_get(i, j + 1).isdigit() else 0
        ])
    
    idx_gear = [(i, j) for i, j in idx_of_star if count_number(i, j) == 2]

    print(idx_gear)