#!/usr/bin/env python3

with open(".input.txt", "r") as file:
    puzzle_input = file.read().splitlines()

search_positions = {
    "ul": (-1, -1),
    "uc": (-1, 0),
    "ur": (-1, 1),
    "ml": (0, -1),
    "mr": (0, 1),
    "dl": (1, -1),
    "dc": (1, 0),
    "dr": (1, 1)
}


def check_bounds(y, x):
    if y < len(puzzle_input) and y >= 0:
        if x < len(puzzle_input[0]) and x >= 0:
            return True
        else: return False
    else: return False


def word_search(coord, puzzle_input, position):
    letters_to_check = ["M", "A", "S"]
    y, x = coord[0] + position[0], coord[1] + position[1]
    for letter in letters_to_check:
        if check_bounds(y, x):
            if puzzle_input[y][x] == letter:
                y, x = y + position[0], x + position[1]
            else: return False
        else: return False
    return True


def main():
    line_count, xmas_count = 0, 0
    for line in puzzle_input:
        character_count = 0
        for character in line:
            if character == "X":
                x_coord = (line_count, character_count)
                for position in search_positions:
                    match = word_search(x_coord, puzzle_input, search_positions[position])
                    if match: 
                        xmas_count += 1
            character_count += 1
        line_count += 1
    print(xmas_count)


if __name__ == "__main__":
    main()
