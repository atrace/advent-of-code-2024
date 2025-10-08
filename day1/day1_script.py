input_file = "day1/day1_input.txt"
line_separator = "   "


location_list_1 = []
location_list_2 = []
total_distance = 0

with open(input_file) as file:
    for line in file:
        locations = line.strip().split(line_separator)
        location_list_1.append(int(locations[0]))
        location_list_2.append(int(locations[1]))

print("🚀 list length 1", len(location_list_1))
print("🚀 list length 2", len(location_list_2))

location_list_1.sort()
location_list_2.sort()

for index in range(len(location_list_1)):
    location1 = location_list_1[index]
    location2 = location_list_2[index]

    total_distance += abs(location1 - location2)

print("🚀 total_distance", total_distance)
