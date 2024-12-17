import re

# Open and read the file
file_path = "2024/14.txt"

with open(file_path, "r") as file:
    file_content = file.read()

ProcessData = lambda file_content:[[int(i) for i in re.findall(r'-?\d+',machine)] for machine in file_content.split('\n')]

# Print the content
robots = ProcessData(file_content)
#print(robots)

def prod(val) : 
    res = 1
    for ele in val: 
        res *= ele 
    return res  


def move_robots(robots,T,r,c):
    s=0
    while s<T:
        move_robots_once(robots,r,c)
        s+=1
    return robots     

def move_robots_once(robots,r,c):
    for robot in robots:
        robot[0]+=robot[2]
        robot[1]+=robot[3]
        robot[0]=robot[0]%r
        robot[1]=robot[1]%c
    return(robots)
    
  

def quad_count(robots):  
    Q1=0
    Q2=0
    Q3=0
    Q4=0
    for robot in robots:
        outr,outc=robot[0],robot[1]
        if outr<(R-1)/2 and outc<(C-1)/2:
            Q1+=1
        elif outr<(R-1)/2 and outc>C/2:
            Q2+=1
        elif outr>R/2 and outc<(C-1)/2:
            Q3+=1
        elif outr>R/2 and outc>C/2:
            Q4+=1
    return Q1,Q2,Q3,Q4


R=101
C=103  
moved_robots=move_robots(robots,100,R,C) 
p1 = prod(list(quad_count(moved_robots)))

p2dist = 1e12
s=0
for i in range(10000):
    if i==0:
        print(robots[0])
    this_dist=prod(list(quad_count(move_robots_once(robots,R,C) )))
    if this_dist < p2dist:
        p2dist=this_dist
        s=i+1
        print(s)

print(p1)
print(p2dist,s)
    