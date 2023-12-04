from pathlib import Path

day = "day1"
puzzle_path = Path("puzzle")

with open(puzzle_path / f"{day}.txt", "r") as puzzle:

    numeric = ([char for char in line if char.isdigit()] for line in puzzle)
    
    result = sum(int(line[0] + line[-1]) for line in numeric)

    print(result)

with open(puzzle_path / f"{day}.debug.1.txt", "r") as puzzle:

    word_mapping = dict(
        one=1,
        two=2,
        three=3,
        four=4,
        five=5,
        six=6,
        seven=7,
        eight=8,
        nine=9
    )
    def first_last_digit(line: str):
        digit_find = sorted([
            (line.find(digit), str(word_mapping.get(digit, digit)))
            for digit
            in list(word_mapping.keys()) + [str(i) for i in word_mapping.values()]
            if line.find(digit) != -1
        ], key=lambda d: d[0])
        return digit_find[0][1] + digit_find[-1][1]

    result = sum(int(first_last_digit(line)) for line in puzzle)

    print(result)
