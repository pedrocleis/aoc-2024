from enum import Enum

f = open("inputs/day06.txt", "r", encoding="utf-8")
map = f.read().split("\n")

def count_x(map):
    visited = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'X':
                visited += 1
    return visited

def find_soldier(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '^':
                return (i, j)

def move_soldier(soldier_pos, soldier_ori, dict_ori, map):
    if map[soldier_pos[0] + dict_ori[soldier_ori][2][0]][soldier_pos[1] + dict_ori[soldier_ori][2][1]] == '#':
        next_ori = dict_ori[soldier_ori][0]
        next_pos = [soldier_pos[0] + dict_ori[soldier_ori][1][0], soldier_pos[1] + dict_ori[soldier_ori][1][1]]
        return (next_ori, next_pos)
    else:
        next_pos = [soldier_pos[0] + dict_ori[soldier_ori][2][0], soldier_pos[1] + dict_ori[soldier_ori][2][1]]
        return (soldier_ori, next_pos)

def part1(map, dict_ori):
    soldier_pos = find_soldier(map)
    solider_ori = '^'
    while (soldier_pos[0] > 0 and soldier_pos[0] < len(map) - 1 and soldier_pos[1] > 0 and soldier_pos[1] < len(map[0]) - 1):
        map[soldier_pos[0]] = list(map[soldier_pos[0]])
        map[soldier_pos[0]][soldier_pos[1]] = 'X'
        map[soldier_pos[0]] = ''.join(map[soldier_pos[0]])
        solider_ori, soldier_pos = move_soldier(soldier_pos, solider_ori, dict_ori, map)
    return count_x(map) + 1

dict_ori = { '^': ('>', [0, +1], [-1, 0]),
            '>': ('v', [+1, 0], [0, +1]),
            'v': ('<', [0, -1], [+1, 0]),
            '<': ('^', [-1, 0], [0, -1])
            }

print(part1(map, dict_ori))