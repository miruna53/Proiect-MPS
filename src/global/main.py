import math

from csv_parser import *
from file import *
from functions import *
import random as rand
import matplotlib.pyplot as plt


def apply_operations(file, order):
    r1 = root1(
        f1(file.thresholds[order[0]], file.thresholds[order[1]], file.thresholds[order[2]], file.optimal_threshold,
           file.f_measures),
        f2(file.thresholds[order[3]], file.thresholds[order[4]], file.thresholds[order[5]], file.optimal_threshold,
           file.f_measures),
        f3(file.thresholds[order[6]], file.thresholds[order[7]], file.thresholds[order[8]], file.optimal_threshold,
           file.f_measures),
        f4(file.thresholds[order[9]], file.thresholds[order[10]], file.thresholds[order[11]], file.optimal_threshold,
           file.f_measures),
        f5(file.thresholds[order[12]], file.thresholds[order[13]], file.thresholds[order[14]], file.optimal_threshold,
           file.f_measures)
        , file.optimal_threshold, file.f_measures)
    r2 = root2(
        f1(file.thresholds[order[0]], file.thresholds[order[1]], file.thresholds[order[2]], file.optimal_threshold,
           file.f_measures),
        f2(file.thresholds[order[3]], file.thresholds[order[4]], file.thresholds[order[5]], file.optimal_threshold,
           file.f_measures),
        f3(file.thresholds[order[6]], file.thresholds[order[7]], file.thresholds[order[8]], file.optimal_threshold,
           file.f_measures),
        f4(file.thresholds[order[9]], file.thresholds[order[10]], file.thresholds[order[11]], file.optimal_threshold,
           file.f_measures),
        f5(file.thresholds[order[12]], file.thresholds[order[13]], file.thresholds[order[14]], file.optimal_threshold,
           file.f_measures)
        , file.optimal_threshold, file.f_measures)

    r3 = (r1 + r2) / 2
    r4 = (r1 * r2) ** (1./2.)

    dif1 = abs(file.f_measures[math.floor(255 * r1)] - file.f_measures[math.floor(255 * file.optimal_threshold)])
    dif2 = abs(file.f_measures[math.floor(255 * r2)] - file.f_measures[math.floor(255 * file.optimal_threshold)])
    dif3 = abs(file.f_measures[math.floor(255 * r3)] - file.f_measures[math.floor(255 * file.optimal_threshold)])
    dif4 = abs(file.f_measures[math.floor(255 * r4)] - file.f_measures[math.floor(255 * file.optimal_threshold)])

    if dif1 == min(dif1, dif2, dif3, dif4):
        return r1
    elif dif2 == min(dif1, dif2, dif3, dif4):
        return r2
    elif dif3 == min(dif1, dif2, dif3, dif4):
        return r3
    elif dif4 == min(dif1, dif2, dif3, dif4):
        return r4


def apply_data_sets(training_files, validation_files, test_files, no_of_orders_generated):
    # initialize first three orders/trees
    initial_order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    first_order = []
    second_order = []
    third_order = []

    first_error = 100
    second_error = 100
    third_error = 100

    # use training set to determine first three best orders/trees
    for i in range(no_of_orders_generated):
        current_order = initial_order
        rand.shuffle(current_order)
        total_error = 0
        for file in training_files:
            error = abs(file.f_measures[math.floor(255 * apply_operations(file, current_order))] - file.f_measures[
                math.floor(255 * file.optimal_threshold)])
            total_error = total_error + error
        current_error = total_error / len(training_files)
        if current_error < first_error:
            third_order = second_order.copy()
            third_error = second_error

            second_order = first_order.copy()
            second_error = first_error

            first_order = current_order.copy()
            first_error = current_error

        elif current_error < second_error:
            third_order = second_order.copy()
            third_error = second_error

            second_order = current_order.copy()
            second_error = current_error

        elif current_error < third_error:
            third_order = current_order.copy()
            third_error = current_error

    print("first order: ", first_order)
    print("first error: ", first_error)
    print("\n")

    print("second order: ", second_order)
    print("second error: ", second_error)
    print("\n")

    print("third order: ", third_order)
    print("third error: ", third_error)
    print("\n")

    first_total_error = 0
    second_total_error = 0
    third_total_error = 0

    # use validation set to determine best order/tree out of the first three
    for file in validation_files:
        first_error = abs(file.f_measures[math.floor(255 * apply_operations(file, first_order))] - file.f_measures[
            math.floor(255 * file.optimal_threshold)])
        first_total_error = first_total_error + first_error

        second_error = abs(file.f_measures[math.floor(255 * apply_operations(file, second_order))] - file.f_measures[
            math.floor(255 * file.optimal_threshold)])
        second_total_error = second_total_error + second_error

        third_error = abs(file.f_measures[math.floor(255 * apply_operations(file, third_order))] - file.f_measures[
            math.floor(255 * file.optimal_threshold)])
        third_total_error = third_total_error + third_error

    first_validation_error = first_total_error / len(validation_files)
    print("first validation error: ", first_validation_error)

    second_validation_error = second_total_error / len(validation_files)
    print("second validation error: ", second_validation_error)

    third_validation_error = third_total_error / len(validation_files)
    print("third validation error: ", third_validation_error)

    best_order = []

    if first_validation_error == min(first_validation_error, second_validation_error, third_validation_error):
        best_order = first_order
    elif second_validation_error == min(first_validation_error, second_validation_error, third_validation_error):
        best_order = second_order
    elif third_validation_error == min(first_validation_error, second_validation_error, third_validation_error):
        best_order = third_order

    # use test set to find out the mean error of the best tree
    total_error = 0
    for file in test_files:
        error = abs(file.f_measures[math.floor(255 * apply_operations(file, best_order))] - file.f_measures[
            math.floor(255 * file.optimal_threshold)])
        total_error = total_error + error
    mean_error = total_error / len(test_files)

    print("mean error: ", mean_error)

    return mean_error


def main():

    training_files = []
    test_files = []
    validation_files = []

    length = len(get_files())

    files = get_files()
    rand.shuffle(files)

    # separate data set intro training, validation and test sets
    i = 0
    for csv_file in files:
        if i < 0.7 * length:
            training_files.append(parse_file(csv_file))
        elif i < 0.95 * length:
            validation_files.append(parse_file(csv_file))
        else:
            test_files.append(parse_file(csv_file))
        i = i + 1

    print("no of training files: ", len(training_files))
    print("no of validation files: ", len(validation_files))
    print("no of test files: ", len(test_files))

    no_of_generated_trees = [10, 100, 1000, 10000, 100000]
    mean_errors = []
    for no in no_of_generated_trees:
        mean_errors.append(apply_data_sets(training_files, validation_files, test_files, no))

    print(mean_errors)

    plt.scatter(no_of_generated_trees, mean_errors)
    plt.xlabel("Number of Generated Trees")
    plt.ylabel("Mean Error for Best Tree")

    plt.xscale('log')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
