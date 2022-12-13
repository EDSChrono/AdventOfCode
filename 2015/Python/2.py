# import data

data = open('2015/2.txt')
lines = [l.strip().split('x') for l in data]

lines_int = []
for l in lines:
    lines_int.append([int(d) for d in l])

wt = 0
bt = 0
for l in lines_int:
    x,y,z = sorted(l)
    # paper for gift
    w = 2*(x*y + y*z + z*x)
    # spare paper
    s = x*y
    # ribbon for present
    rp = 2*(x  +y)
    # ribbon for bow
    rb = x*y*z
    # update totals
    wt += w+s
    bt += rb+rp

# p1
print(wt)

# p2
print(bt)