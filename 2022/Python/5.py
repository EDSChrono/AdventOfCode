# define functions
def transpose_stack_data(lines):
    stack_list = []
    for line in lines:
        # stop when we reach an empty line
        if line == '':
            break
        no_stacks = (len(line)+1)//4
        # make empty sublist for stacks
        while len(stack_list) < no_stacks:
            stack_list.append([])
        # populate stack with label if applicable
        for stack in range(no_stacks):
            box_label = line[1+4*stack]
            if 'A'<=box_label<='Z':
                stack_list[stack].append(box_label)
    return(stack_list)

def apply_crate_moves(stack_list, lines, rev = True):
    found = False
    for cmd in lines:
        if cmd == '':
            found = True 
            continue
        if not found:
            continue
        words = cmd.split()
        qty = int(words[1])
        s_from = int(words[3])-1
        s_to = int(words[5])-1
        crates_to_move = stack_list[s_from][:qty]
        stack_list[s_from] = stack_list[s_from][qty:]
        stack_list[s_to] = (list(reversed(crates_to_move)) if rev else crates_to_move) + stack_list[s_to]
    return(stack_list)

# import data
data = open('2022/5.txt').read()
lines = [x for x in data.split('\n')]

# transform stacks to list of lists
stack_list = transpose_stack_data(lines)

# apply transformation (add false argument from p2)
rearr_stack_list = apply_crate_moves(stack_list, lines, True)

# output code
print(''.join(rearr_stack_list[i][0] for i in range(len(rearr_stack_list))))


