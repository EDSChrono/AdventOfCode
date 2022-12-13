
# build function

def comp(p1,p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            return -1
        if p1 > p2:
            return +1
        else:
            return 0
    elif isinstance(p1, list) and isinstance(p2, list):
        i=0
        while i < min(len(p1), len(p2)):
            c = comp(p1[i],p2[i])
            if c != 0:
                return c
            i+=1
        if len(p1)==i and len(p2)>i:
            return -1
        elif len(p2)==i and len(p1)>i:
            return 1
        else:
            return 0
    elif isinstance(p1, int) and isinstance(p2, list):
        return comp([p1],p2)
    elif isinstance(p1, list) and isinstance(p2, int):
        return comp(p1,[p2])

def index_sum_sorted_pairs(input):
    output = 0
    for index,pair in enumerate(input.split('\n\n')):
        p1,p2 = pair.split('\n')
        p1 = eval(p1)
        p2 = eval(p2)
        if comp(p1,p2)==-1:
            output += index+1
    return output

def list_all_packets(input,dp1,dp2):
    output = [dp1,dp2]
    for pair in input.split('\n\n'):
        p1,p2 = pair.split('\n')
        p1 = eval(p1)
        p2 = eval(p2)
        output.append(p1)
        output.append(p2)
    return output

def sort_packets(input):
    iterate = True
    while iterate:
        iter_count = 0
        for i in range(len(input) - 1):
            p1 = input[i]
            p2 = input[i+1]
            if comp(p1, p2) == 1:
                input[i] = p2
                input[i+1] = p1
                iter_count += 1
        iterate = iter_count>0
    return input

def decoder_key(input, p1, p2):
    output = 1
    for index,packet in enumerate(input):
        if packet == p1 or packet == p2:
            output *= (index+1)
    return output


 # import data       
data = open('2022/13.txt').read().strip()
dp1,dp2 = [[2]],[[6]]

# calculate part 1
part1 = index_sum_sorted_pairs(data)
print(part1)

# calculate part 2
all_packets = list_all_packets(data,dp1,dp2)
sorted_packets = sort_packets(all_packets)
part2 = decoder_key(sorted_packets,dp1,dp2) 
print(part2)
