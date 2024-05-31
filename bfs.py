from collections import deque


def bfs_tsp(cities, distances):
    num_cities = len(cities)
    min_cost = float('inf')
    min_path = []

    queue = deque([(0, [0], 0)])  # (current city, path, current cost)

    while queue:
        current_city, path, cost = queue.popleft()

        if len(path) == num_cities:
            cost += distances[current_city][0]  # return to the starting city
            if cost < min_cost:
                min_cost = cost
                min_path = path + [0]
            continue

        for next_city in cities:
            if next_city not in path:
                new_cost = cost + distances[current_city][next_city]
                queue.append((next_city, path + [next_city], new_cost))

    return min_path, min_cost