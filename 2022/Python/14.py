
# build function
def sign(x):
    if x == 0:
        return 0
    elif x>0:
        return 1
    else:
        return -1

# import data       
data = open('2022/14.txt').read().strip()
lines = data.split('\n')

# set up rocks
rocks = set()
ymax = 0
for l in lines:
    c = l.split(' -> ')
    for r in range(len(c)-1):
        xs,ys = c[r].split(',')
        xs,ys = int(xs),int(ys)
        xe,ye = c[r+1].split(',')
        xe,ye = int(xe),int(ye)
        dy = ye-ys
        dx = xe-xs
        ymax = max(ymax, ye, ys)
        q = max(abs(dy),abs(dx))
        for d in range(q+1):
            rocks.add((xs + sign(dx)*d,ys + sign(dy)*d))

# set up floor - remove for p1
for x in range(2*(ymax+2)+1):
    rocks.add((500-ymax+x-2,ymax+2))

# count rocks pre-sand
no_rocks = len(rocks)

# sand
ymax+=2 # remove for p1
iterate=True
while iterate:
    sx = 500
    sy = 0
    while sy<ymax: # prevent freefall
        if (sx,sy+1) not in rocks:
            sy+=1
        elif (sx-1,sy+1) not in rocks:
            sx-=1
            sy+=1
        elif (sx+1,sy+1) not in rocks:  
            sx+=1
            sy+=1
        else:
            rocks.add((sx,sy))
            break
    iterate = sy != ymax and (500,0) not in rocks # remove 2nd test for p1
    
answer = print(len(rocks) - no_rocks)