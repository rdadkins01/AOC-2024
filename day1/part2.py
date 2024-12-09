
with open("input.txt") as file:
    input = file.read().splitlines()

list1 = []
list2 = []

for line in input:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

list1, list2 = sorted(list1), sorted(list2)
similarity_score = 0

for list1_num in list1:
    match_count = 0
    for list2_num in list2:
        if list1_num == list2_num:
            match_count += 1
    similarity_score += list1_num * match_count

print(f'The "Similarity Scsore" between the two lists is: {similarity_score}')
