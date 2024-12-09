
with open("input.txt") as file:
    input = file.read().splitlines()

list1 = []
list2 = []

for line in input:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

list1, list2 = sorted(list1), sorted(list2)
distance_variance = 0
max_locations = len(list1)
count = 0

while max_locations > count:
    distance_variance +=  abs(list1[count] - list2[count])
    count += 1

print(f'"Distance" between the two lists is: {distance_variance}')
