import time
from io_utils import read_from_file, write_to_file
from tsp import solve_tsp

def main():
    input_file_path = 'input'  # input file path
    output_file_path = 'output'  # output file path

    # start time of the program
    program_start_time = time.time()

    # read input data
    cities, distances = read_from_file(input_file_path)

    # solve TSP
    results = solve_tsp(cities, distances)

    # the end time of the program
    program_end_time = time.time()
    total_execution_time = program_end_time - program_start_time
    results['Total_execution_time'] = total_execution_time

    # write to the output file
    write_to_file(output_file_path, results)

if __name__ == "__main__":
    main()
