
with open(".input.txt", "r") as file:
    input = file.read()

list_of_values = []


def find_next_multiple(input):
    final_value = False

    multiply_start_index = input.find("mul(")
    print(f"Start Index: {multiply_start_index}")

    multiply_value_separator = input.find(",",multiply_start_index)
    print(f"Multiple Value Separator: {multiply_value_separator}")

    multiply_first_value = input[multiply_start_index + 4:multiply_value_separator]
    print(f"First Value: {multiply_first_value}")

    multiply_end_index = input.find(")", multiply_start_index)
    print(f"End Index: {multiply_end_index}")

    multiply_second_value = input[multiply_value_separator + 1:multiply_end_index]
    print(f"Second Value: {multiply_second_value}")

    next_multiply_start = input.find("mul(", multiply_start_index + 4)
    print(f"Next Start Index: {next_multiply_start}")

    if next_multiply_start == -1: final_value = True

    if not final_value:
        if next_multiply_start < multiply_end_index:
            return 0, multiply_start_index, multiply_start_index + 4
    
    print(type(next_multiply_start))


    try:
        return int(multiply_first_value) * int(multiply_second_value), multiply_start_index, multiply_end_index

    except:
        print("   Invalid number in multiples!")
        return 0, multiply_start_index, multiply_end_index


while "mul(" in input:
    print(input)
    result, multiply_start_index, multiply_end_index = find_next_multiple(input)
    list_of_values.append(result)

    input = input[:multiply_start_index] + input[multiply_end_index:]

print(list_of_values)

value_count = 0

for value in list_of_values:
    value_count += value

print(value_count)