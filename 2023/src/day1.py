from pathlib import Path

day = "day1"
puzzle_path = Path("puzzle")

with open(puzzle_path / f"{day}.txt", "r", encoding="utf-8") as puzzle:
    numeric = ([char for char in line if char.isdigit()] for line in puzzle)

    result = sum(int(line[0] + line[-1]) for line in numeric)

    print(result)

with open(puzzle_path / f"{day}.txt", "r", encoding="utf-8") as puzzle:
    word_mapping = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    def modify_line(line: str):
        for val, word in enumerate(word_mapping):
            line = line.replace(word, f"{word}{val+1}{word}")
        return line

    numeric = (
        [char for char in modify_line(line) if char.isdigit()] for line in puzzle
    )
    result = sum(int(line[0] + line[-1]) for line in numeric)

    print(result)
