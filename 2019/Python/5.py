
def gravity_assist(ic,n,v,pmode=0):
    intcode = ic[:]
    i = 0
    intcode[1] = n
    intcode[2] = v
    while all([j<len(intcode) for j in range(i,i+4)]):
        opcode = intcode[i]
        if opcode == 99:
            return intcode[0]
        if opcode == 1:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
            i+=4
        elif opcode == 2:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
            i+=4
        elif opcode == 3:
            intcode[intcode[i+1]] = input
            i+=2
        elif opcode == 4:
            output = intcode[intcode[i+1]]
            i+=2
    return 'Something went wrong'

data = open('2019/2.txt').read()

integers = data.split(',')
integers = [int(x) for x in integers]

# p1
print(gravity_assist(integers,12,2))

# p2
target = 19690720
for n in range(100):
    for v in range(100):
        if gravity_assist(integers,n,v) == target:
            print(100 * n + v)

