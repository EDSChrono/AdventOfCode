
# function to turn input lines into integer vector of endpoints
def input_string_to_vector(assign_pair_string):
    endpoint_vector = []
    for line in assign_pair_string:
        assign_list_1,assign_list_2 = line.split(',')
        l1,u1= assign_list_1.split('-')
        l2,u2= assign_list_2.split('-')
        endpoint_vector.append([int(x) for x in [l1,u1,l2,u2]])
    return endpoint_vector

# function to count pairs based on nested and distinct criteria
def assign_pair_count(assign_pair_endpoints):
    count_nest = 0
    count_dist = 0
    for line in assign_pair_endpoints:
        l1,u1,l2,u2= line
        if not (u1 < l2 or l1 > u2):
            count_dist += 1
        if l1<=l2 and u2<=u1 or l2<=l1 and u1<=u2:
            count_nest += 1
    return count_nest, count_dist


# import data
lines = [line.strip() for line in open('2022/4.txt')]

# convert input
endpoint_list = input_string_to_vector(lines)

# p1 & p2
print(assign_pair_count(endpoint_list))