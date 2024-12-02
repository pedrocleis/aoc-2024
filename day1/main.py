f = open("inputs/day1.txt", "r", encoding="utf-8")
locations = f.read().split("\n")
left_locations = []
right_locations = []

def part1(locations ):
  for location in locations:
    split_location = (location.split("   "))
    left_locations.append(split_location[0])
    right_locations.append(split_location[1])

  left_locations.sort()
  right_locations.sort()

  total_distance = 0

  for i in range(len(left_locations)):
    total_distance += abs(int(left_locations[i]) - int(right_locations[i]))

  return(total_distance)

print(part1(locations))