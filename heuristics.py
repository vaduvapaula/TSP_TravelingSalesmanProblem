def heuristic(path, cities, distances):
    remaining_cities = set(cities) - set(path)
    if not remaining_cities:
        return 0
    current_city = path[-1]
    heuristic_cost = 0
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: distances[current_city][city])
        heuristic_cost += distances[current_city][next_city]
        current_city = next_city
        remaining_cities.remove(next_city)
    heuristic_cost += distances[current_city][0]  # return to start city
    return heuristic_cost