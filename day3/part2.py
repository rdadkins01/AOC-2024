#!/usr/bin/env python3
import re


def text_search(input_string, search_string):
    '''
    input_string is from the puzzle input
    search_string is expecting mul(), do() or don't()
    outputs a dictionary in the following formats:
    do()/don't(): {start_index: count, ...}
    mul(): {start_index: [list of values], ...}
    '''
    out_dict = {}
    count = 1

    if search_string == "mul()":
        regex_string = "mul\(\d+\,\d+\)"
    if search_string == "do()":
        regex_string = "do\(\)"
    if search_string == "don't()":
        regex_string = "don\'t\(\)"

    match = re.search(fr"{regex_string}", input_string)
    first_run = True
    running_index = 0
    while match != None:

        if search_string == "mul()":
            match_string = match.group()
            first_val = int(match_string.split(",")[0].split("(")[1])
            second_val = int(match_string.split(",")[1].split(")")[0])
            if not first_run:
                out_dict[match.start() + running_index] = [first_val, second_val]
            else:
                out_dict[match.start()] = [first_val, second_val]
                first_run = False

        elif "do" in search_string:
            if not first_run:
                out_dict[match.start() + running_index] = count
            else:
                out_dict[match.start()] = count
                first_run = False
            count += 1
            
        running_index += len(match.group())

        input_string = input_string[:match.start()] + input_string[match.end():]
        match = re.search(regex_string, input_string)

    return out_dict


def main():
    with open(".input.txt", "r") as file:
        input = file.read().replace("\n", "")

    enable = True
    total = 0
    muls = text_search(input, "mul()")
    dos = text_search(input, "do()")
    donts = text_search(input, "don't()")

    current_do_max = float("-inf")
    current_dont_max = float("-inf")

    for mul in muls:
        for do in dos:
            if do < mul:
                current_do_max = do

        for dont in donts:
            if dont < mul:
                current_dont_max = dont

        if current_do_max < current_dont_max:
            enable = False

        if current_do_max > current_dont_max:
            enable = True

        if enable:
            total += muls[mul][0] * muls[mul][1]

    print(total)

if __name__ == "__main__":
    main()
