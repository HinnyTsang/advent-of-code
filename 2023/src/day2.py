from typing import Tuple
from pathlib import Path
from functools import lru_cache

day = "day2"
puzzle_path = Path("puzzle")

color_limit = {
    'red': 12,
    'green': 13,
    'blue': 14
}

@lru_cache(2)
def parse_row(row: str) -> Tuple[bool, int]:
    game, cubes = row.split(':')
    _, game_id = game.split()
    cubes = cubes.split(';')
    cubes_bags = (cube.strip().split(', ') for cube in cubes)
    possible = all(
        all(
            color_limit.get(bag.split()[1]) >= int(bag.split()[0])
            for bag in bags
        )
        for bags in cubes_bags
    )
    return possible, int(game_id)

with open(puzzle_path / f"{day}.txt", "r") as puzzle:
   
    print(sum(parse_row(line)[1] for line in puzzle if parse_row(line)[0]))

