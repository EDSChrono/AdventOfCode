grid = []
with open("2024/10.txt", "r") as file:
    for line in file:
        grid.append([int(x) for x in line.strip()])  # Convert each line into a list
    
    
def peak_finder(G,r,c,S=set(),step=0,T=0):
    if G[r][c] != step:
        return(S,T)
    if step == 9:
        S.add((r,c))
        T+=1
        return(S,T)
    if r+1 < len(G):
        if G[r+1][c] == step+1:
            ST = peak_finder(G,r+1,c,S,step+1,T)
            S | ST[0]
            T = ST[1]
    if r-1 >= 0:
        if G[r-1][c] == step+1:
            ST = peak_finder(G,r-1,c,S,step+1,T)
            S | ST[0]
            T = ST[1]
    if c+1 < len(G[r]):
        if G[r][c+1] == step+1:
            ST = peak_finder(G,r,c+1,S,step+1,T)
            S | ST[0]
            T = ST[1]
    if c-1 >= 0:
        if G[r][c-1] == step+1:
            ST = peak_finder(G,r,c-1,S,step+1,T)
            S | ST[0]
            T = ST[1]
    return(S,T)

p1 = 0
p2 = 0
 
for r in range(len(grid)):
    for c in range(len(grid[r])):
        peaksreached = set()
        output = peak_finder(grid,r,c,peaksreached)
        p1 += len(output[0])
        p2 += output[1]
        
print(p1)
print(p2)     