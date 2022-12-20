from collections import deque

data = open('2022/18.txt').read().strip()
lines = [x for x in data.split('\n')]
coords=set()
from collections import deque

def in_surface(sc,a,b,c,O=False,co='',R=5000):
    if O:
        for r in range(R):
            if co == '+x':
                if in_surface(sc,a+r,b,c):
                    return True
            if co == '-x':
                if in_surface(sc,a-r,b,c):
                    return True
            if co == '+y':
                if in_surface(sc,a,b+r,c):
                    return True
            if co == '-y':
                if in_surface(sc,a,b-r,c):
                    return True
            if co == '+z':
                if in_surface(sc,a,b,c+r):
                    return True
            if co == '-z':
                if in_surface(sc,a,b,c-r):
                    return True

    else:
        return (a,b,c) in sc





for l in lines:
    x,y,z = l.split(',')
    x,y,z = int(x),int(y),int(z)
    coords.add((x,y,z))

SA = 0
for x,y,z in coords:
    if not in_surface(coords,x+1,y,z,True,'+x'):
        SA+=1
    if not in_surface(coords,x-1,y,z,True,'-x'):
        SA+=1
    if not in_surface(coords,x,y+1,z,True,'+y'):
        SA+=1
    if not in_surface(coords,x,y-1,z,True,'-y'):
        SA+=1
    if not in_surface(coords,x,y,z+1,True,'+z'):
        SA+=1
    if not in_surface(coords,x,y,z-1,True,'-z'):
        SA+=1

OUT = set()
IN = set()
def reaches_outside(x,y,z,part):
    if (x,y,z) in OUT:
        return True
    if (x,y,z) in IN:
        return False
    SEEN = set()
    Q = deque([(x,y,z)])
    while Q:
        x,y,z = Q.popleft()
        if (x,y,z) in coords:
            continue
        if (x,y,z) in SEEN:
            continue
        SEEN.add((x,y,z))
        if len(SEEN) > (5000 if part==2 else 0):
            for p in SEEN:
                OUT.add(p)
            return True
        Q.append((x+1,y,z))
        Q.append((x-1,y,z))
        Q.append((x,y+1,z))
        Q.append((x,y-1,z))
        Q.append((x,y,z+1))
        Q.append((x,y,z-1))
    for p in SEEN:
        IN.add(p)
    return False

SA = 0
for (x,y,z) in coords:
    if reaches_outside(x+1,y,z,2):
        SA += 1
    if reaches_outside(x-1,y,z,2):
        SA += 1
    if reaches_outside(x,y+1,z,2):
        SA += 1
    if reaches_outside(x,y-1,z,2):
        SA += 1
    if reaches_outside(x,y,z+1,2):
        SA += 1
    if reaches_outside(x,y,z-1,2):
        SA += 1
        
print(SA)