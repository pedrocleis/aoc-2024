f = open("inputs/day1.txt", "r", encoding="utf-8")
locations = f.read().split("\n")
left_locations = []
right_locations = []

def part1(left_locations, right_locations):
  left_locations.sort()
  right_locations.sort()

  total = 0

  for i in range(len(left_locations)):
    total += abs(int(left_locations[i]) - int(right_locations[i]))

  return(total)

def part2(left_locations, right_locations):
  total = 0
  
  for lefty in left_locations:
    count = right_locations.count(lefty)
    total += count * int(lefty)

  return total

for location in locations:
  split_location = (location.split("   "))
  left_locations.append(split_location[0])
  right_locations.append(split_location[1])

print(part1(left_locations, right_locations))
print(part2(left_locations, right_locations))