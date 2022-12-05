
#Define functions
def scorer(selection_list, options_op, options_me):
    score = 0
    for op,me in selection_list:
        me_index = options_me.index(me)
        op_index = options_op.index(op)
        score += options_me.index(me) + 1 + 3 * ((me_index-op_index + 1)%3)
    return score
   
def selection_adj(selection_list, options_op, options_me):
    for index,x in enumerate(selection_list):
        selection_list[index][1] = options_me[(options_op.index(x[0]) + options_me.index(x[1]) - 1)%3]
    return selection_list 

#Process Inputs
input_list = [l.strip() for l in open('2022/2.txt')]
input_list_split = [x.split() for x in input_list]

#Reference Tables
options_op = ['A','B','C']
options_me = ['X','Y','Z']

#P1
print(scorer(input_list_split, options_op, options_me))

#P2
adj_input_list_split = selection_adj(input_list_split, options_op, options_me)
print(scorer(adj_input_list_split, options_op, options_me))