grid = []
with open("2024/12.txt", "r") as file:
    for line in file:
        grid.append([x for x in line.strip()])
    
    
def region_identify(G,r,c,S):
    S.add((r,c))
    for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
        if 0<=r+dr<len(G) and 0<=c+dc<len(G[0]):
            if G[r+dr][c+dc]==G[r][c] and (r+dr,c+dc) not in S:
                S.add((r+dr,c+dc))
                region_identify(G,r+dr,c+dc,S)
    return S           
            
            
def region_score(S):
    p=0
    for s in S:
        pc=4
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]: 
            nexts = list(s)[0]+dr,list(s)[1]+dc
            if nexts in S:
                pc-=1
        p+=pc
    return p * len(S)

def region_score_disc(S):
    p=0
    for s in S:
        pc=0
        nr=[(1,0),(0,-1),(-1,0),(0,1)]
        for i in range(len(nr)):
            dr1,dc1=nr[i]
            dr2,dc2=nr[(i+1)%len(nr)] 
            nexts1 = list(s)[0]+dr1,list(s)[1]+dc1
            nexts2 = list(s)[0]+dr2,list(s)[1]+dc2
            nexts3 = list(s)[0]+dr1+dr2,list(s)[1]+dc1+dc2
            if nexts1 not in S and nexts2 not in S:
                pc+=1
            if ((nexts1 in S) ^ (nexts2 in S)) and nexts3 in S:
                pc+=0.5
        p+=pc
    return p * len(S)

def fencing_price(G,apply_discount=False):
    TotalScore=0
    regsets=set()
    for r in range(len(G)):
        for c in range(len(G[r])):
            S=set()
            countsets=len(regsets)
            reg=region_identify(G,r,c,S)
            regsets.add(frozenset(reg))
            if len(regsets)-countsets==1:
                if apply_discount:
                    score=region_score_disc(reg)
                else:
                    score=region_score(reg) 
                TotalScore+=score  
    return TotalScore           

p1 = fencing_price(grid)   
p2 = fencing_price(grid,True)        

print(p1,p2)      
    