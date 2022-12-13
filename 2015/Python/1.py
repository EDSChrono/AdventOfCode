# functions
def req_floor(input):
    while "()" in input or ")(" in input:
        input = input.replace("()","")
        input = input.replace(")(","")
    return len(input)

def when_base(data):
    level = 0
    i = 0
    while level >= 0:
        if data[i] == "(":
            level+=1
        else:
            level-=1
        i+=1
    return i

# import data
data = open('2015/1.txt').read()

# part 1
p1 = req_floor(data)
print(p1)

# part 2
p2 = when_base(data)
print(p2)
