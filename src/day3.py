f = open("inputs/day3.txt", "r", encoding="utf-8")
inputs = f.read().split("\n")

def main (inputs) :
    total_part1 = 0
    total_part2 = 0
    enabled = True
    for line in inputs:
        for i in range(len(line)):
            if line[i] == 'd':
                if line[i+1] == 'o':
                    if line[i+2] == '(':
                        if line[i+3] == ')':
                            enabled = True
                    elif line[i+2] == 'n':
                        if line[i+3] == "'":
                            if line[i+4] == 't':
                                if line[i+5] == '(':
                                    if line[i+6] == ')':
                                        enabled = False

            elif line[i] == 'm':
                if line[i+1] == 'u':
                    if line[i+2] == 'l':
                        if  line[i+3] == '(':
                            first_number = ''
                            if line[i+4].isdigit(): # (1
                                first_number += line[i+4]
                                if line[i+5].isdigit(): # (11
                                    first_number += line[i+5]
                                    if line[i+6] == ',': # (11,
                                        second_number = ''
                                        if line[i+7].isdigit(): # (11,1
                                            second_number += line[i+7]
                                            if line[i+8] == ')':
                                                total_part1 += int(first_number) * int(second_number)
                                                if enabled:
                                                    total_part2 += int(first_number) * int(second_number)
                                            elif line[i+8].isdigit(): # (11,11
                                                second_number += line[i+8]
                                                if line[i+9] == ')':
                                                    total_part1 += int(first_number) * int(second_number)
                                                    if enabled:
                                                        total_part2 += int(first_number) * int(second_number)
                                                elif line[i+9].isdigit(): # (11,111
                                                    second_number += line[i+9]
                                                    if line[i+10] == ')':
                                                        total_part1 += int(first_number) * int(second_number)
                                                        if enabled:
                                                            total_part2 += int(first_number) * int(second_number)
                                    elif line[i+6].isdigit(): # (111
                                        first_number += line[i+6]
                                        if line[i+7] == ',':
                                            second_number = ''
                                            if line[i+8].isdigit(): # (111,1
                                                second_number += line[i+8]
                                                if line[i+9] == ')': # (111,1)
                                                    total_part1 += int(first_number) * int(second_number)
                                                    if enabled:
                                                        total_part2 += int(first_number) * int(second_number)
                                                elif line[i+9].isdigit(): # (111,11
                                                    second_number += line[i+9]
                                                    if line[i+10] == ')': # (111,11)
                                                        total_part1 += int(first_number) * int(second_number)
                                                        if enabled:
                                                            total_part2 += int(first_number) * int(second_number)
                                                    elif line[i+10].isdigit(): # (111,111
                                                        second_number += line[i+10]
                                                        if line[i+11] == ')': # (111,111)
                                                            total_part1 += int(first_number) * int(second_number)
                                                            if enabled:
                                                                total_part2 += int(first_number) * int(second_number)
                                elif  line[i+5] == ',' : # (1,
                                    second_number = ''
                                    if line[i+6].isdigit(): # (1,1
                                        second_number += line[i+6]
                                        if line[i+7] == ')': # (1,1)
                                            total_part1 += int(first_number) * int(second_number)
                                            if enabled:
                                                total_part2 += int(first_number) * int(second_number)
                                        elif line[i+7].isdigit(): # (1,11
                                            second_number += line[i+7]
                                            if line[i+8] == ')': # (1,11)
                                                total_part1 += int(first_number) * int(second_number)
                                                if enabled:
                                                    total_part2 += int(first_number) * int(second_number)
                                            elif line[i+8].isdigit(): # (1,111
                                                second_number += line[i+8]
                                                if line[i+9] == ')': # (1,111)
                                                    total_part1 += int(first_number) * int(second_number)
                                                    if enabled:
                                                        total_part2 += int(first_number) * int(second_number)
    return total_part1, total_part2

print(main(inputs))
