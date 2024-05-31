def read_from_file(file_path):
    """read cities and distances from input file"""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        cities = list(map(int, lines[0].split()))
        distances = [list(map(int, line.split())) for line in lines[1:]]
    return cities, distances

def write_to_file(file_path, results):
    """write the results to the output file"""
    with open(file_path, 'w') as file:
        for algorithm, result in results.items():
            if 'time' not in algorithm and algorithm != 'Total_execution_time':
                path, cost = result
                file.write(f"{algorithm} Path: {path}\n")
                file.write(f"{algorithm} Cost: {cost}\n")
                file.write(f"{algorithm} Execution Time: {results[algorithm + '_time']:.6f} seconds\n\n")
        file.write(f"Total Execution Time: {results['Total_execution_time']:.6f} seconds\n") # total time
