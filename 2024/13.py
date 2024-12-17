import re

file_path = "2024/13.txt"

with open(file_path, "r") as file:
    file_content = file.read()

ProcessData = lambda file_content:[[int(i) for i in re.findall(r'\d+',machine)] for machine in file_content.split('\n'*2)]

values = ProcessData(file_content)


def min_token(v,isP2=False):
    if isP2:
        v[4]+=10000000000000
        v[5]+=10000000000000
    b=(v[4]*v[1]-v[5]*v[0])/(v[2]*v[1]-v[3]*v[0])
    a=(v[4]-b*v[2])/v[0]
    if a==int(a) and b==int(b):
        return int(3*a + b)
    else:
        return 0 

p1=0
p2=0
for v in values:
    p1+=min_token(v)
    p2+=min_token(v,True)
    
print(p1,p2)
