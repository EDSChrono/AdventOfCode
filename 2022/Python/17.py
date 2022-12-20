import re
import copy
import math

wind_dir = open('2022/17.txt').read().strip()

####
def get_block(b,h):
    if b==0:
        return set([(2,h),(3,h),(4,h),(5,h)])
    if b==1:
        return set([(3,h),(2,h+1),(3,h+1),(4,h+1),(3,h+2)])
    if b==2:
        return set([(2,h),(3,h),(4,h),(4,h+1),(4,h+2)])
    if b==3:
        return set([(2,h),(2,h+1),(2,h+2),(2,h+3)])
    if b==4:
        return set([(2,h),(3,h),(2,h+1),(3,h+1)])

def move_right(b):
    if any([x==6 for (x,y) in b]):
        return b
    else:
        return set([(x+1,y) for (x,y) in b])

def move_left(b):
    if any([x==0 for (x,y) in b]):
        return b
    else:
        return set([(x-1,y) for (x,y) in b])

def move_down(b):
    return set([(x,y-1) for (x,y) in b])

def base_sig(S,r):
    ymax = []
    for x in range(r):
        S_x = {(xS,yS) for (xS,yS) in S if xS == x}
        ym = -1
        for s in S_x:
            if s[1]>ym:
                ym=s[1]
        ymax.append(ym)
    yminmax=min(ymax)
    full_row = set()
    for x in range(r):
        full_row.add((x,yminmax) in S)
    if all(full_row):
        S = S - {(x,y) for (x,y) in S if y<yminmax}
        S = {(x,y-yminmax) for (x,y) in S}
    return S

def hash_sig(S,i,w):
    return hash(str([S,i,w]))

def signature(R):
    maxY = max([y for (x,y) in R])
    return frozenset([(x,maxY-y) for (x,y) in R if maxY-y<=30])

def main(wd,h,nb):
    i=0
    sigs = []
    outsigs=[]
    w=0
    base = set([(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),(5,-1),(6,-1)])
    b=get_block(0,h)
    while i<nb:
        if wd[w] == '>':
            new_block_cand=move_right(b)
            if len(new_block_cand.intersection(base))==0:
                b=new_block_cand
        elif wd[w] == '<':
            new_block_cand=move_left(b)
            if len(new_block_cand.intersection(base))==0:
                b=new_block_cand    
        new_block_cand = move_down(b)
        if len(new_block_cand.intersection(base))>0:
            new_block = b
            base = base.union(new_block)
            h=max([y for (x,y) in base]) + 4
            i+=1
            new_sig=hash_sig(signature(base),i%5,w%len(wind_dir))
            if new_sig in sigs:
                sigs.append(new_sig)
                for index,s in enumerate(sigs):
                    if s == new_sig:
                        outsigs.append(index)
                #return h-3,outsigs
            else:
                sigs.append(new_sig)
            b=get_block(i%5,h)
        else:
            b = new_block_cand
        w=(w+1)%len(wd)
    return h-3,outsigs

#cycle_out = print(main(wind_dir,3,3200))
#cadence = cycle_out[1][1]-cycle_out[1][0]
#print(main(wind_dir,3,cadence)*(1000000000000//cadence) + main(wind_dir,3,(1000000000000%cadence)))
x = (1000000000000//1700)*2623 + main(wind_dir,3,1000000000000%1700)[0]
print(x)

