import copy
def not_beacon(x,y,Sensor_Range):
    for [sx,sy,d] in Sensor_Range:
        dxy = abs(x-sx)+abs(y-sy)
        if dxy<=d:
            return True
    return False

# import data       
data = open('2022/15.txt').read().strip()
lines = data.split('\n')

Beacons = set()
sb = []
max_x=-1e9
min_x=1e9
max_y=-1e9
min_y=1e9

# get beacons
for l in lines:
    c = [k.split('=')[1] for k in l.split(' ') if '=' in k]
    c = [int(k.replace(",","").replace(":","")) for k in c]
    absx = abs(c[2]-c[0])
    absy = abs(c[3]-c[1])
    d_bs = absx + absy
    Beacons.add((c[2],c[3]))
    c = c[0:2]
    max_x=max(max_x,c[0]+d_bs)
    min_x=min(min_x,c[0]-d_bs)
    c.append(d_bs)
    sb.append(c)

y_r = 2e6

# p1=0
# for x in range(min_x,max_x):
#     if not_beacon(x,y_r,sb) and (x,y_r) not in B:
#         p1+=1
    
# print(p1)

m = 4e6
BreakFlag = False
for i in sb:
    for d in range(i[2]+2):
        dx = d
        dy = i[2]+1-d
        for sx,sy in [(-1,1),(1,1),(1,-1),(-1,-1)]:
            x = i[0]+dx*sx
            y = i[1]+dy*sy
            if 0<=x<=m and 0<=y<=m:
                if not not_beacon(x,y,sb) and not BreakFlag:
                    output = (x,y)
                    BreakFlag = True


print(4e6*output[0] + output[1])
