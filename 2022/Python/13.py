
# build comparison function
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
    

 # import data       
data = open('2022/13.txt').read().strip()

# calculate part 1
part1 = 0
all_packets = [[[2]],[[6]]]
for index,pair in enumerate(data.split('\n\n')):
    p1,p2 = pair.split('\n')
    p1 = eval(p1)
    p2 = eval(p2)
    all_packets.append(p1)
    all_packets.append(p2)
    if comp(p1,p2)==-1:
        part1 += index+1

print(part1)

# calculate part 2
iterate = True
while iterate:
    iter_count = 0
    for i in range(len(all_packets) - 1):
        p1 = all_packets[i]
        p2 = all_packets[i+1]
        if comp(p1, p2) == 1:
            all_packets[i] = p2
            all_packets[i+1] = p1
            iter_count += 1
    iterate = iter_count>0

part2 = 1
for index,packet in enumerate(all_packets):
    if packet == [[2]] or packet == [[6]]:
        part2 *= (index+1)

print(part2)
    



