#Define Functions
def score(c):
    score_output = ord(c.upper())-ord('A') + 1 + 26 * int('A'<=c<='Z')
    return score_output

def priority(string_list):
    result = 0
    for string in string_list:
        comp_length = len(string)/2
        assert int(comp_length) == comp_length
        c_1,c_2 = string[:comp_length], string[comp_length:]
        for char in c_1:
            if char in c_2:
                result += score(char)
                break
    return result

def priority_sum(string_list, group_size):
    assert len(string_list)%group_size == 0
    result = 0
    group_index = 0
    while group_index < len(string_list): 
        for char in string_list[group_index]:
            if char in string_list[group_index+1] and char in string_list[group_index+2]:
                result += score(char)
                break
        group_index += group_size
    return result

#Import Data
bag_manifest = [line.strip() for line in open('2022/3.txt')]

#P1
print(priority(bag_manifest))

#P2
print(priority_sum(bag_manifest, 3))
