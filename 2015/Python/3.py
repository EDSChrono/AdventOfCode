# import data
data = open('2015/3.txt').read()

def increment_house(x, y, houses):
    if (x, y) in houses:
        houses[(x, y)] += 1
    else:
        houses[(x, y)] = 1

def calc_move(x, y, move):
    if move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    elif move == '>':
        x += 1
    else:
        x -= 1
    return x, y

santaX = 0
santaY = 0
robX = 0
robY = 0
houses = {}
increment_house(santaX, santaY, houses)
increment_house(robX, robY, houses)

for index,char in enumerate(data):
    # in p1 set mod to 1 
    if index%2 == 0:
        santaX, santaY = calc_move(santaX, santaY, char)
        increment_house(santaX, santaY, houses)
    else:
        robX, robY = calc_move(robX, robY, char)
        increment_house(robX, robY, houses)
print(len(houses))

