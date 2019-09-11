import matplotlib.pyplot as plt
import csv 
import glob
import sys
import pandas as pd
import seaborn as sns
import numpy as np
import os


def plot_state_values(input_file_pattern, output_dir_path):
    state_values = []
    for i, file_path in enumerate(glob.glob(input_file_pattern)):
        state_values.append([])
        with open(file_path, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                state_values[i].append(list(map(float, row)))    
    state_values_arr = np.array(state_values)
    mean_state_values = np.average(state_values_arr, axis=0)
    plt.figure()
    sns.heatmap(mean_state_values, annot=True)
    output_file_path = os.path.join(output_dir_path, os.path.splitext(os.path.basename(file_path))[0] + ".png")
    plt.savefig(output_file_path)
    plt.close()
    print(f"export values to {output_file_path}")
    # TODO show


def main():
    argvs = sys.argv[1:]
    # file_pattern = "res/steps/SubGoalFourrooms-v0*steps.csv"
    n_episodes = 2000
    mean_y = []
    sum_y = []
    steps_file_patterns = [os.path.join("res", "steps", argv) for argv in argvs]
    values_file_patterns = [os.path.join("res", "values", argv) for argv in argvs]

    for i, file_pattern in enumerate(steps_file_patterns):
        # import pdb; pdb.set_trace()
        mean_y.append([0] * n_episodes)
        sum_y.append([0] * n_episodes)
        for run, file_path in enumerate(glob.glob(file_pattern+'*')):
            with open(file_path, "r", encoding='utf-8') as f:
                reader = csv.reader(f)
                for step, row in enumerate(reader):
                    mean_y[i][step] = 1/(1+run) * (run * mean_y[i][step] + int(row[0]))
                    sum_y[i][step] += int(row[0])

    for i, value_file_pattern in enumerate(values_file_patterns):
        plot_state_values(value_file_pattern + '*', "res/values")

    plt.plot(list(range(n_episodes)), mean_y[i], label=file_pattern)
    plt.legend()
    plt.ylim(0, 1000)
    plt.legend()
    # plt.show()
    plt.savefig(file_path.split('/')[-1] + '.png')
    print(file_path.split('/')[-1] + '.png')
    plt.close()
    

if __name__ == "__main__":
    main()