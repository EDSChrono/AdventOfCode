import fileinput, heapq

# Construct the grid from the input file
grid = { (x, y): char
         for y, row in enumerate(fileinput.input("2024/16.txt"))
         for x, char in enumerate(row.strip('\n')) }

# Find the starting position ('S')
start_position = min(pos for pos, value in grid.items() if value == 'S')

# Priority queue for the pathfinding algorithm
priority_queue = [(0, start_position, 0)]  # (cost, position, direction)

# Best cost dictionary to track the lowest cost to reach a state
best_cost = {(start_position, 0): 0}

# Path reconstruction dictionary
predecessors = {(start_position, 0): []}

while priority_queue:
    current_cost, current_position, current_direction = heapq.heappop(priority_queue)

    # If we reach the end ('E')
    if grid[current_position] == 'E':
        solution_states = set([(current_position, current_direction)])

        # Trace back the path
        while True:
            predecessors_to_add = set(predecessor for state in solution_states for predecessor in predecessors[state])
            if predecessors_to_add.issubset(solution_states):
                break
            solution_states.update(predecessors_to_add)

        # Print the final cost and the number of unique positions visited
        print(current_cost, len(set(pos for pos, direction in solution_states)))
        break

    # Skip if this state has already been visited with a lower cost
    if best_cost[(current_position, current_direction)] < current_cost:
        continue

    # Possible moves: turn left, turn right, or move forward
    moves = [
        (current_cost + 1000, current_position, (current_direction - 1) % 4),  # Turn left
        (current_cost + 1000, current_position, (current_direction + 1) % 4),  # Turn right
        (current_cost + 1, (current_position[0] + (1, 0, -1, 0)[current_direction],
                            current_position[1] + (0, 1, 0, -1)[current_direction]), current_direction)  # Move forward
    ]

    for new_cost, new_position, new_direction in moves:
        if grid.get(new_position) != '#':  # Ensure the new position is not a wall
            # If the new state has not been visited or a better cost is found
            if (new_position, new_direction) not in best_cost or best_cost[(new_position, new_direction)] > new_cost:
                best_cost[(new_position, new_direction)] = new_cost
                predecessors[(new_position, new_direction)] = [(current_position, current_direction)]
                heapq.heappush(priority_queue, (new_cost, new_position, new_direction))

            # If the new state has the same cost, add to the predecessors for alternative paths
            elif best_cost[(new_position, new_direction)] == new_cost:
                predecessors[(new_position, new_direction)].append((current_position, current_direction))