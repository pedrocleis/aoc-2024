f = open("inputs/day4.txt", "r", encoding="utf-8")
puzzle = f.read().split("\n")

def part1(puzzle):
    xmas = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 'X':
                try:
                    if j + 3 < len(puzzle[i]) and puzzle[i][j+1] == 'M' and puzzle[i][j+2] == 'A' and puzzle[i][j+3] == 'S':
                        xmas += 1 # HORIZONTAL ->
                    if j - 3 >= 0 and puzzle[i][j-1] == 'M' and puzzle[i][j-2] == 'A' and puzzle[i][j-3] == 'S':
                        xmas += 1 # HORIZONTAL <-
                    if i + 3 < len(puzzle) and puzzle[i+1][j] == 'M' and puzzle[i+2][j] == 'A' and puzzle[i+3][j] == 'S':
                        xmas += 1 # VERTICAL DOWN
                    if i - 3 >= 0 and puzzle[i-1][j] == 'M' and puzzle[i-2][j] == 'A' and puzzle[i-3][j] == 'S':
                        xmas += 1 # VERTICAL UP
                    if i + 3 < len(puzzle) and j + 3 < len(puzzle[i]) and puzzle[i+1][j+1] == 'M' and puzzle[i+2][j+2] == 'A' and puzzle[i+3][j+3] == 'S':
                        xmas += 1 # DIAGONAL DOWN RIGHT
                    if i - 3 >= 0 and j - 3 >= 0 and puzzle[i-1][j-1] == 'M' and puzzle[i-2][j-2] == 'A' and puzzle[i-3][j-3] == 'S':
                        xmas += 1 # DIAGONAL UP LEFT
                    if i + 3 < len(puzzle) and j - 3 >= 0 and puzzle[i+1][j-1] == 'M' and puzzle[i+2][j-2] == 'A' and puzzle[i+3][j-3] == 'S':
                        xmas += 1 # DIAGONAL DOWN LEFT
                    if i - 3 >= 0 and j + 3 < len(puzzle[i]) and puzzle[i-1][j+1] == 'M' and puzzle[i-2][j+2] == 'A' and puzzle[i-3][j+3] == 'S':
                        xmas += 1 # DIAGONAL UP RIGHT
                except IndexError:
                    pass
    return xmas

def part2(puzzle):
    xmas = 0
    for i in range (len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 'A':
                try:
                    if (i-1 >= 0 and j-1 >= 0 and i+1 <= len(puzzle) and j+1 <= len(puzzle[i])) and ((puzzle[i-1][j-1] == 'S' and puzzle[i+1][j+1] == 'M') or (puzzle[i+1][j+1] == 'S' and puzzle[i-1][j-1] == 'M')): # -- ++, ++ --
                        if (i-1 >= 0 and j-1 >= 0 and i+1 <= len(puzzle) and j+1 <= len(puzzle[i])) and (puzzle[i+1][j-1] == 'S' and puzzle[i-1][j+1] == 'M') or (puzzle[i-1][j+1] == 'S' and puzzle[i+1][j-1] == 'M'): # +- -+, -+ +-
                            xmas += 1
                        else:
                            pass
                    else:
                        pass
                except IndexError:
                    pass
    return xmas
        

print(part1(puzzle))
print(part2(puzzle))