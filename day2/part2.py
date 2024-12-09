
with open("input.txt", "r") as file:
    input = file.read().splitlines()

unsafe_count = 0
safe_count = 0


def report_check(report):
    level_next = 1
    level_current = 0
    unsafe = False
    current_direction = ""
    while level_next < len(report): 
        last_direction = current_direction # Keep track of directions
        if not unsafe:
            level_change = int(report[level_next]) - int(report[level_current])
            if level_change < 0: current_direction = "decrease"
            elif level_change > 0: current_direction = "increase"
            unsafe = safety_check(level_change, current_direction, last_direction, level_current)

        level_next += 1
        level_current += 1

    return unsafe


def safety_check(level_change, current_direction, last_direction, level_current):
    '''
    Returns whether the level is unsafe (Bool)
    '''
    if level_change == 0: 
        return True

    if level_current != 0: # Direction changes can't occur on the first round.
        if current_direction != last_direction: # Check for direction changes
            return True

    if abs(level_change) < 1 or abs(level_change) > 3:
        return True

    return False


def problem_dampener(report, index):
    # Function created just to have a reason to use "problem_dampener"
    removed_level = report[index]
    report.pop(index)
    return report, removed_level


for report in input:
    report = report.split()
    unsafe = report_check(report)
    halt_dampener = False

    if unsafe:
        count = 0
        while len(report) > count:
            if not halt_dampener:
                dampened_report, removed_level = problem_dampener(report, count)
                unsafe = report_check(report)
                if not unsafe:
                    halt_dampener = True
                
                repair_report = report.insert(count, removed_level)
            count += 1


    if unsafe: unsafe_count += 1
    else: safe_count += 1

print(f"\nThere are {safe_count} safe reports and {unsafe_count} unsafe reports.")
