import fileinput, heapq

grid = { (x, y): char
         for y, row in enumerate(fileinput.input("2024/16.txt"))
         for x, char in enumerate(row.strip('\n')) }

start_position = min(pos for pos, value in grid.items() if value == 'S')

priority_queue = [(0, start_position, 0)] 

best_cost = {(start_position, 0): 0}

predecessors = {(start_position, 0): []}

while priority_queue:
    current_cost, current_position, current_direction = heapq.heappop(priority_queue)

    if grid[current_position] == 'E':
        solution_states = set([(current_position, current_direction)])

        while True:
            predecessors_to_add = set(predecessor for state in solution_states for predecessor in predecessors[state])
            if predecessors_to_add.issubset(solution_states):
                break
            solution_states.update(predecessors_to_add)

        print(current_cost, len(set(pos for pos, direction in solution_states)))
        break

    if best_cost[(current_position, current_direction)] < current_cost:
        continue

    moves = [
        (current_cost + 1000, current_position, (current_direction - 1) % 4),  
        (current_cost + 1000, current_position, (current_direction + 1) % 4),  
        (current_cost + 1, (current_position[0] + (1, 0, -1, 0)[current_direction],
                            current_position[1] + (0, 1, 0, -1)[current_direction]), current_direction) 
    ]

    for new_cost, new_position, new_direction in moves:
        if grid.get(new_position) != '#':  
            if (new_position, new_direction) not in best_cost or best_cost[(new_position, new_direction)] > new_cost:
                best_cost[(new_position, new_direction)] = new_cost
                predecessors[(new_position, new_direction)] = [(current_position, current_direction)]
                heapq.heappush(priority_queue, (new_cost, new_position, new_direction))

            elif best_cost[(new_position, new_direction)] == new_cost:
                predecessors[(new_position, new_direction)].append((current_position, current_direction))