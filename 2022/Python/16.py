import re
import copy

def bfs(start, end):
    depth = 1
    while True:
        next_step = set()
        for x in start:
            if x == end:
                return depth
            for y in valves[x]['tunnels']:
                next_step.add(y)
        start = next_step
        depth += 1

data = open('2022/16.txt').read().strip()
lines = data.split('\n')

valves={}

for l in lines:
    x=re.split('Valve | has|=|;| valves | valve ',l)
    valves[x[1]] = {'flow':int(x[3]), 'tunnels': x[5].split(', '),'paths': {}}

keys = sorted([x for x in list(valves.keys()) if valves[x]['flow'] != 0])

for k in keys + ['AA']:
    for k2 in keys:
        if k2 != k:
            valves[k]['paths'][k2] = bfs(valves[k]['tunnels'], k2)

current_valve = 'AA'
time_remaining = 27
flow_rate = 0
flow_accum = 0
valves_opened = set()
def flow_count(v,v_o,t_r,c_v,fr,fa):
    v_o2 = copy.deepcopy(v_o)
    while t_r > 0:
        if c_v not in v_o2:
           fa+=fr
           fr+=v[c_v]['flow']
           v_o2.add(c_v)
           t_r-=1
        else:
            bv = 0
            v_bv = ''
            for nv in v[c_v]['paths'].keys() - v_o2:
                vv = flow_count(v,v_o2,t_r-v[c_v]['paths'][nv],nv,fr,fa+min(v[c_v]['paths'][nv],t_r)*fr)[0]
                if vv>bv:
                    v_bv = nv
                    bv = max(bv,vv)
            if bv == 0:
                fa+=fr
                t_r-=1
            else:
                fa+=fr*min(v[c_v]['paths'][v_bv],t_r)
                t_r-=v[c_v]['paths'][v_bv]
                c_v=v_bv
    return fa,v_o2

p1 = flow_count(valves,valves_opened,time_remaining,current_valve,flow_rate,flow_accum)
p2 = flow_count(valves,p1[1],time_remaining-1,current_valve,flow_rate,flow_accum)
print(p1,p2)
print(p1[0]+p2[0])
