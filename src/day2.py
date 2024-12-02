f = open("inputs/day2.txt", "r", encoding="utf-8")
registers = f.read().split("\n")

def safe_register(register):
  ascending = register[0] < register[1]
  for i in range(len(register) -1):
    if (ascending):
      if (register[i] > register[i+1]):
        return False
    else:
      if (register[i] < register[i+1]):
        return False

    if (abs(register[i] - register[i+1]) > 3):
      return False
    elif (abs(register[i] - register[i+1]) == 0):
      return False
  
  return True

def dampener(register):
  count = 0
  for i in range(len(register)):
    if (safe_register(register[:i] + register[i+1:])):
      count += 1

  return count == 1 or count == 2


def main(registers):
  total = 0
  total_day2 = 0
  for register in registers:
    split_register = list(map(int, register.split(" ")))
    if (safe_register(split_register)):
      total += 1
    elif (dampener(split_register)):
      total_day2 += 1
    
  total_day2 += total

  return total, total_day2

print(main(registers))
# print(dampener([8, 6, 4, 4, 1]))

