from functools import cache
import time

pebbles = []
with open("2024/11.txt", "r") as file:
    pebbles = [int(x) for x in file.readline().split()]
    
@cache
def count_pebbles(p,c):
    if c==0:
        return 1
    if p==0:
        return count_pebbles(1,c-1)
    if len(str(p))%2 == 0:
        sp=str(p)
        return count_pebbles(int(sp[len(sp)//2:]),c-1)+count_pebbles(int(sp[:len(sp)//2]),c-1)
    else:
        return count_pebbles(p*2024,c-1)

start_time = time.time()

p1=0
p2=0
    
for pebble in pebbles:
    p1+=count_pebbles(pebble,25)
    p2+=count_pebbles(pebble,75)
    
end_time = time.time()
    
print(p1)
print(p2)
print(end_time-start_time)
    
    
