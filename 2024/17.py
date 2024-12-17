import re
import math

file_path = "2024/17.txt"

with open(file_path, "r") as file:
    file_content = file.read()

ProcessData = lambda content: [
    [int(i) for i in re.findall(r'\d+', content.split("\n\n")[0])],
    [int(i) for i in re.findall(r'\d+', content.split("\n\n")[1])]
]
data = ProcessData(file_content)

def find_combo_operand(literal_operand, registers):
    if literal_operand < 4:
        return literal_operand
    elif literal_operand == 4:
        return registers[0]
    elif literal_operand == 5:
        return registers[1]
    elif literal_operand == 6:
        return registers[2]
    else:
        raise ValueError(f"Invalid literal operand: {literal_operand}")

def apply_instruction(instruction, literal_operand, registers, instruction_pointer, outputs=[]):
    if instruction == 0:  # adv
        combo_operand = find_combo_operand(literal_operand, registers)
        registers[0] = math.trunc(registers[0] / (2 ** combo_operand))
        instruction_pointer += 2
    elif instruction == 1:  # bxl
        registers[1] = registers[1]^literal_operand
        instruction_pointer += 2
    elif instruction == 2:  # bst
        registers[1] = find_combo_operand(literal_operand, registers) % 8
        instruction_pointer += 2
    elif instruction == 3:  # jnz
        if registers[0] != 0:
            instruction_pointer = literal_operand
        else:
            instruction_pointer += 2
    elif instruction == 4:  # bxc
        registers[1] = registers[1]^registers[2]
        instruction_pointer += 2
    elif instruction == 5:  # out
        outputs.append(find_combo_operand(literal_operand, registers) % 8)
        instruction_pointer += 2
    elif instruction == 6:  # bdv
        combo_operand = find_combo_operand(literal_operand, registers)
        registers[1] = math.trunc(registers[0] / (2 ** combo_operand))
        instruction_pointer += 2
    elif instruction == 7:  # cdv
        combo_operand = find_combo_operand(literal_operand, registers)
        registers[2] = math.trunc(registers[0] / (2 ** combo_operand))
        instruction_pointer += 2
    return instruction_pointer, registers, outputs

ip = 0
registers = data[0]
program = data[1]
output = []

while ip < len(program):
    ip, registers, output = apply_instruction(program[ip], program[ip + 1], registers, ip, output)

print('p1='+','.join(map(str, output)))

possibleanswers={0}
for x in range(len(program)):
    possibleanswersx=possibleanswers.copy()
    for pa in possibleanswers:
        possibleanswersx.remove(pa)
        for a in range(8):
            rega=(pa*2**3)+a
            ip=0
            output=[]
            registers=[rega,0,0]
            while ip < len(program):
                ip, registers, output = apply_instruction(program[ip], program[ip + 1], registers, ip, output)
            if output[:x+1]==program[-(x+1):]:
                possibleanswersx.add(rega)
    possibleanswers=possibleanswersx
    
print('p2='+str(min(list(possibleanswers))))
            
    
