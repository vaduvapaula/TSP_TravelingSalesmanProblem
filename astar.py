# astar.py

import heapq
from heuristics import heuristic

def astar_tsp(cities, distances):
    num_cities = len(cities)
    min_cost = float('inf')
    min_path = []

    pq = [(0, 0, [0])]  # (f = g + h, g = cost so far, path)

    while pq:
        f, g, path = heapq.heappop(pq)
        current_city = path[-1]

        if len(path) == num_cities:
            g += distances[current_city][0]  # return to the starting city
            if g < min_cost:
                min_cost = g
                min_path = path + [0]
            continue

        for next_city in cities:
            if next_city not in path:
                new_g = g + distances[current_city][next_city]
                h = heuristic(path + [next_city], cities, distances)
                new_f = new_g + h
                heapq.heappush(pq, (new_f, new_g, path + [next_city]))

    return min_path, min_cost