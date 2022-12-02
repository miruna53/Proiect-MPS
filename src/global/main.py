import math

from csv_parser import *
from file import *
from functions import *
import random as rand


def apply_operations(file, order):
    r1 = root1(
        f1(file.thresholds[order[0]], file.thresholds[order[1]], file.thresholds[order[2]], file.optimal_threshold, file.f_measures),
        f2(file.thresholds[order[3]], file.thresholds[order[4]], file.thresholds[order[5]], file.optimal_threshold, file.f_measures),
        f3(file.thresholds[order[6]], file.thresholds[order[7]], file.thresholds[order[8]], file.optimal_threshold, file.f_measures),
        f4(file.thresholds[order[9]], file.thresholds[order[10]], file.thresholds[order[11]], file.optimal_threshold, file.f_measures),
        f5(file.thresholds[order[12]], file.thresholds[order[13]], file.thresholds[order[14]], file.optimal_threshold, file.f_measures)
        , file.optimal_threshold, file.f_measures)
    r2 = root2(
        f1(file.thresholds[order[0]], file.thresholds[order[1]], file.thresholds[order[2]], file.optimal_threshold, file.f_measures),
        f2(file.thresholds[order[3]], file.thresholds[order[4]], file.thresholds[order[5]], file.optimal_threshold, file.f_measures),
        f3(file.thresholds[order[6]], file.thresholds[order[7]], file.thresholds[order[8]], file.optimal_threshold, file.f_measures),
        f4(file.thresholds[order[9]], file.thresholds[order[10]], file.thresholds[order[11]], file.optimal_threshold, file.f_measures),
        f5(file.thresholds[order[12]], file.thresholds[order[13]], file.thresholds[order[14]], file.optimal_threshold, file.f_measures)
        , file.optimal_threshold, file.f_measures)

    dif1 = abs(file.f_measures[math.floor(255 * r1)] - file.f_measures[math.floor(255 * file.optimal_threshold)])
    dif2 = abs(file.f_measures[math.floor(255 * r2)] - file.f_measures[math.floor(255 * file.optimal_threshold)])

    if dif1 < dif2:
        return r1
    else:
        return r2


def main():
    training_files = []
    test_files = []
    validation_files = []

    length = len(get_files())

    files = get_files()
    # rand.shuffle(files)

    i = 0
    for csv_file in files:
        if i < 0.7 * length:
            training_files.append(parse_file(csv_file))
        elif i < 0.95 * length:
            validation_files.append(parse_file(csv_file))
        else:
            test_files.append(parse_file(csv_file))
        i = i + 1

    print(len(training_files))
    print(len(validation_files))
    print(len(test_files))

    initial_order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    best_order = initial_order
    best_error = 100

    for i in range(1000):
        current_order = initial_order
        rand.shuffle(current_order)
        total_error = 0
        for file in training_files:
            error = abs(file.f_measures[math.floor(255 * apply_operations(file, current_order))] - file.f_measures[
                math.floor(255 * file.optimal_threshold)])
            total_error = total_error + error
        mean_error = total_error / len(training_files)
        if mean_error < best_error:
            best_error = mean_error
            best_order = current_order

    print(best_order)
    print(best_error)
    print("\n")

    total_error = 0

    for file in validation_files:
        error = abs(file.f_measures[math.floor(255 * apply_operations(file, best_order))] - file.f_measures[math.floor(255 * file.optimal_threshold)])
        total_error = total_error + error

    mean_error = total_error / len(validation_files)
    print(mean_error)


if __name__ == "__main__":
    main()
