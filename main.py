import csv
import numpy
import os
import glob


def load_values(file_path):
    values = []
    reader = csv.reader()
        for row in reader:
            values.append(row)
    return values




def main():
    subgoal_value_map = [[(3,6), ""], [(6,2), ""], [(7,9), ""], [(10,6), ""]]
    subgoal_order_indexes = [[1,3], [2,4]]
    all_values = []
    for index, file_path in subgoal_value_map:
        values = load_values(file_path)
        all_values.append(values)
    


if __name__ == "__main__":
    main()