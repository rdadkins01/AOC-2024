#!/usr/bin/env python3

with open(".input.txt", "r") as file:
    puzzle_input = file.read().splitlines()

search_positions = {
    "uldr": [(-1, -1),(1, 1)],
    "urdl": [(-1, 1),(1, -1)],
    "dlur": [(1, -1),(-1, 1)],
    "drul": [(1, 1),(-1, -1)]
}


def check_bounds(y, x):
    if y < len(puzzle_input) and y >= 0:
        if x < len(puzzle_input[0]) and x >= 0: return True
        else: return False
    else: return False


def word_search(coord, puzzle_input, positions):
    letters_to_check = ["M", "S"]
    # Check if M or S
    pos_index = 0
    y, x = coord[0] + positions[0][0], coord[1] + positions[0][1]
    if check_bounds(y, x):
        if puzzle_input[y][x] == "M":
            y, x = coord[0] + positions[1][0], coord[1] + positions[1][1]
            if check_bounds(y, x):
                if puzzle_input[y][x] == "S":
                    return True
                else: return False
            else: return False
        else: return False
    else: return False


def main():
    line_count, xmas_count = 0, 0
    for line in puzzle_input:
        character_count = 0
        for character in line:
            x_leg1, x_leg2 = False, False
            if character == "A":
                coord = (line_count, character_count)
                for positions in search_positions:
                    if not x_leg1:
                        # If first leg hasn't been found, search
                        x_leg1 = word_search(coord, puzzle_input, search_positions[positions])
                    elif not x_leg2:
                        # If first leg has been found, search for second leg
                        x_leg2 = word_search(coord, puzzle_input, search_positions[positions])
                if x_leg1 and x_leg2:
                    xmas_count += 1
            character_count += 1
        line_count += 1
    print(xmas_count)


if __name__ == "__main__":
    main()
