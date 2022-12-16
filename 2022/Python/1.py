
#Define functions
def sorted_calorie_aggregate(input_string_list):
    total_calories_by_elf = []
    for elf in input_string_list:
        elf_total = 0
        for elf_calories in elf.split('\n'):
            elf_total += int(elf_calories)
        total_calories_by_elf.append(elf_total)
    total_calories = sorted(total_calories_by_elf)
    return total_calories

def aggregate_top_n(input, n):
    top_n_sum = 0
    for t_c in range(n):
        top_n_sum += input[-(t_c + 1)]
    return top_n_sum

#Parse data 
rawdata = [l.strip() for l in open('2022/1.txt')]
append_new_line = '\n'.join(rawdata).split('\n\n')

# Main code
total_calories = sorted_calorie_aggregate(append_new_line)

#Part 1&2
print(aggregate_top_n(total_calories, 1))
print(aggregate_top_n(total_calories, 3))
