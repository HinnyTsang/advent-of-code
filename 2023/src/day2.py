from typing import Tuple
from pathlib import Path
from functools import lru_cache
from math import prod

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

@lru_cache(2)
def parse_row_two(row: str) -> Tuple[bool, int]:
    game, cubes = row.split(':')
    _, game_id = game.split()
    cubes = cubes.split(';')
    bags = (cube.strip().split(', ') for cube in cubes)
    bags = [{color.split()[1]: int(color.split()[0]) for color in bag} for bag in bags]
    min_cube = [ 
        max(bag.get(color, 0) for bag in bags)
        for color in color_limit.keys()
    ]
    return prod(min_cube) 

with open(puzzle_path / f"{day}.txt", "r") as puzzle:
    print(sum(parse_row(line)[1] for line in puzzle if parse_row(line)[0]))

with open(puzzle_path / f"{day}.txt", "r") as puzzle:
    print(sum(parse_row_two(line) for line in puzzle))

