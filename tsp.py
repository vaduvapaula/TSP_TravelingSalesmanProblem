import time
from bfs import bfs_tsp
from ucs import ucs_tsp
from astar import astar_tsp

def solve_tsp(cities, distances):
    """results of TSP problem using BFS, UCS, and A*"""
    results = {}

    # bfs time
    start_time = time.time()
    results['BFS'] = bfs_tsp(cities, distances)
    end_time = time.time()
    results['BFS_time'] = end_time - start_time

    # ucs time
    start_time = time.time()
    results['UCS'] = ucs_tsp(cities, distances)
    end_time = time.time()
    results['UCS_time'] = end_time - start_time

    # a* time
    start_time = time.time()
    results['A*'] = astar_tsp(cities, distances)
    end_time = time.time()
    results['A*_time'] = end_time - start_time

    return results
