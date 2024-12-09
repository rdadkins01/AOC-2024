
with open("input.txt", "r") as file:
    input = file.read().splitlines()

unsafe_count = 0
safe_count = 0

for report in input:
    level_next = 1
    level_current = 0
    unsafe = False
    current_direction = ""
    report = report.split()
    while level_next < len(report):
        last_direction = current_direction # Keep track of directions
        if not unsafe:
            
            level_change = int(report[level_next]) - int(report[level_current])

            if level_change < 0: current_direction = "decrease"
            elif level_change > 0: current_direction = "increase"
            elif level_change == 0: unsafe = True

            if level_current != 0: # Direction changes can't occur on the first round.
                if current_direction != last_direction: # Check for direction changes
                    unsafe = True

            if abs(level_change) < 1 or abs(level_change) > 3:
                unsafe = True

        level_next += 1
        level_current += 1

    if unsafe: unsafe_count += 1
    else: safe_count += 1

print(f"There are {safe_count} safe reports and {unsafe_count} unsafe reports.")
