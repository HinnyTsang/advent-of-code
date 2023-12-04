from pathlib import Path

day = "day1"
puzzle_path = Path("puzzle")

with open(puzzle_path / f"{day}.txt", "r") as puzzle:

    numeric = ([char for char in line if char.isdigit()] for line in puzzle)
    
    result = sum(int(line[0] + line[-1]) for line in numeric if line)

    print(result)
