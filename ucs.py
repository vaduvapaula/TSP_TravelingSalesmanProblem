import heapq


def ucs_tsp(cities, distances):
    num_cities = len(cities)
    min_cost = float('inf')
    min_path = []

    pq = [(0, 0, [0])]  # (current cost, current city, path)

    while pq:
        cost, current_city, path = heapq.heappop(pq)

        if len(path) == num_cities:
            cost += distances[current_city][0]  # return to the starting city
            if cost < min_cost:
                min_cost = cost
                min_path = path + [0]
            continue

        for next_city in cities:
            if next_city not in path:
                new_cost = cost + distances[current_city][next_city]
                heapq.heappush(pq, (new_cost, next_city, path + [next_city]))

    return min_path, min_cost
