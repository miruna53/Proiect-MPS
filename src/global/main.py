import math

from csv_parser import *
from file import *
from functions import *
import random as rand
import itertools


def apply_operations(file, order):
    return root1(
        f1(file.thresholds[order[0]], file.thresholds[order[1]], file.thresholds[order[2]], file.optimal_threshold, file.f_measures),
        f2(file.thresholds[order[3]], file.thresholds[order[4]], file.thresholds[order[5]], file.optimal_threshold, file.f_measures),
        f3(file.thresholds[order[6]], file.thresholds[order[7]], file.thresholds[order[8]], file.optimal_threshold, file.f_measures),
        f4(file.thresholds[order[9]], file.thresholds[order[10]], file.thresholds[order[11]], file.optimal_threshold, file.f_measures),
        f5(file.thresholds[order[12]], file.thresholds[order[13]], file.thresholds[order[14]], file.optimal_threshold, file.f_measures)
        , file.optimal_threshold, file.f_measures)


def main():
    files = []

    for csv_file in get_files():
        files.append(parse_file(csv_file))

    initial_order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    best_order = initial_order
    best_error = 100

    for current_order in itertools.permutations(initial_order, len(initial_order)):
        total_error = 0
        for file in files:
            print(current_order)
            error = abs(file.f_measures[math.floor(255 * apply_operations(file, current_order))] - file.f_measures[
                math.floor(255 * file.optimal_threshold)])
            total_error = total_error + error
        mean_error = total_error / len(files)
        if mean_error < best_error:
            best_error = mean_error
            best_order = current_order

    print(best_order)
    print(best_error)


if __name__ == "__main__":
    main()
