from csv_local_parser import *
from LocalFile import *
import random as rand
from LocalFunctions import *
from datetime import datetime


def get_f_measure_for_a_file(order, file):
    true_positives = 0
    true_negatives = 0
    false_positives = 0
    false_negatives = 0
    for pixel in file.get_pixel_list():
        threshold1 = root1(f1(pixel.thresholds[order[0]], pixel.thresholds[order[1]]),
                          f2(pixel.thresholds[order[2]], pixel.thresholds[order[3]]),
                          f3(pixel.thresholds[order[4]], pixel.thresholds[order[5]]),
                          f4(pixel.thresholds[order[6]], pixel.thresholds[order[7]]),
                          f5(pixel.thresholds[order[8]], pixel.thresholds[order[9]]))
        threshold2 = root2(f1(pixel.thresholds[order[0]], pixel.thresholds[order[1]]),
                           f2(pixel.thresholds[order[2]], pixel.thresholds[order[3]]),
                           f3(pixel.thresholds[order[4]], pixel.thresholds[order[5]]),
                           f4(pixel.thresholds[order[6]], pixel.thresholds[order[7]]),
                           f5(pixel.thresholds[order[8]], pixel.thresholds[order[9]]))

        threshold = (threshold1 + threshold2) / 2

        computed_value = 0
        if threshold <= pixel.pixel_value:
            computed_value = 1

        if pixel.pixel_class == 1 and pixel.pixel_class == computed_value:
            true_positives = true_positives + 1

        if pixel.pixel_class == 0 and pixel.pixel_class == computed_value:
            true_negatives = true_negatives + 1

        if pixel.pixel_class == 1 and pixel.pixel_class != computed_value:
            false_negatives = false_negatives + 1

        if pixel.pixel_class == 0 and pixel.pixel_class != computed_value:
            false_positives = false_positives + 1

    f_measure = true_positives / (true_positives + 0.5 * (false_positives + false_negatives))
    return f_measure


def apply_data_sets(training_files, validation_files, test_files, no_of_orders_generated):
    # initialize first three orders/trees
    initial_order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    first_order = []
    second_order = []
    third_order = []

    first_f_measure = 0
    second_f_measure = 0
    third_f_measure = 0

    # use training set to determine first three best orders/trees
    for i in range(no_of_orders_generated):
        current_order = initial_order
        rand.shuffle(current_order)
        total_f_measure = 0
        for file in training_files:
            f_measure = get_f_measure_for_a_file(current_order, file)
            total_f_measure = total_f_measure + f_measure
        current_f_measure = total_f_measure / len(training_files)
        if current_f_measure > first_f_measure:
            third_order = second_order.copy()
            third_f_measure = second_f_measure

            second_order = first_order.copy()
            second_f_measure = first_f_measure

            first_order = current_order.copy()
            first_f_measure = current_f_measure

        elif current_f_measure > second_f_measure:
            third_order = second_order.copy()
            third_f_measure = second_f_measure

            second_order = current_order.copy()
            second_f_measure = current_f_measure

        elif current_f_measure > third_f_measure:
            third_order = current_order.copy()
            third_f_measure = current_f_measure

    print("first order: ", first_order)
    print("first f_measure: ", first_f_measure)
    print("\n")

    print("second order: ", second_order)
    print("second f_measure: ", second_f_measure)
    print("\n")

    print("third order: ", third_order)
    print("third f_measure: ", third_f_measure)
    print("\n")

    first_total_f_measure = 0
    second_total_f_measure = 0
    third_total_f_measure = 0

    # use validation set to determine best order/tree out of the first three
    for file in validation_files:
        first_f_measure = get_f_measure_for_a_file(first_order, file)
        first_total_f_measure = first_total_f_measure + first_f_measure

        second_f_measure = get_f_measure_for_a_file(second_order, file)
        second_total_f_measure = second_total_f_measure + second_f_measure

        third_f_measure = get_f_measure_for_a_file(third_order, file)
        third_total_f_measure = third_total_f_measure + third_f_measure

    first_validation_error = first_total_f_measure / len(validation_files)
    print("first validation f_measure: ", first_validation_error)

    second_validation_error = second_total_f_measure / len(validation_files)
    print("second validation f_measure: ", second_validation_error)

    third_validation_error = third_total_f_measure / len(validation_files)
    print("third validation f_measure: ", third_validation_error)

    best_order = []

    if first_validation_error == max(first_validation_error, second_validation_error, third_validation_error):
        best_order = first_order
    elif second_validation_error == max(first_validation_error, second_validation_error, third_validation_error):
        best_order = second_order
    elif third_validation_error == max(first_validation_error, second_validation_error, third_validation_error):
        best_order = third_order

    # use test set to find out the mean error of the best tree
    total_f_measure = 0
    for file in test_files:
        f_measure = get_f_measure_for_a_file(best_order, file)
        total_f_measure = total_f_measure + f_measure
    mean_f_measure = total_f_measure / len(test_files)

    print("mean f_measure: ", mean_f_measure)

    best_order.append(mean_f_measure)

    return best_order


def main():

    training_files = []
    test_files = []
    validation_files = []

    csv_files = get_files()
    rand.shuffle(csv_files)
    length = len(csv_files)

    i = 0
    for csv_file in csv_files:
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

    best_order = apply_data_sets(training_files, validation_files, test_files, 100)

    print("best order: ", best_order)


if __name__ == "__main__":
    main()
