from csv_parser import *
from file import *
from functions import *


def apply_operations(file):
    # print(f1(file.thresholds[0], file.thresholds[1], file.thresholds[2], file.optimal_threshold, file.f_measures))
    # print(f2(file.thresholds[3], file.thresholds[4], file.thresholds[5], file.optimal_threshold, file.f_measures))
    # print(f3(file.thresholds[6], file.thresholds[7], file.thresholds[8], file.optimal_threshold, file.f_measures))
    # print(f4(file.thresholds[9], file.thresholds[10], file.thresholds[11], file.optimal_threshold, file.f_measures))
    # print(f5(file.thresholds[12], file.thresholds[13], file.thresholds[14], file.optimal_threshold, file.f_measures))
    return root1(
        f1(file.thresholds[0], file.thresholds[1], file.thresholds[2], file.optimal_threshold, file.f_measures),
        f2(file.thresholds[3], file.thresholds[4], file.thresholds[5], file.optimal_threshold, file.f_measures),
        f3(file.thresholds[6], file.thresholds[7], file.thresholds[8], file.optimal_threshold, file.f_measures),
        f4(file.thresholds[9], file.thresholds[10], file.thresholds[11], file.optimal_threshold, file.f_measures),
        f5(file.thresholds[12], file.thresholds[13], file.thresholds[14], file.optimal_threshold, file.f_measures)
        , file.optimal_threshold, file.f_measures)


def main():
    files = []

    for csv_file in get_files():
        files.append(parse_file(csv_file))

    print(apply_operations(files[0]))

    print(files[0].f_measures[math.floor(255 * apply_operations(files[0]))])
    print(files[0].f_measures[math.floor(255 * files[0].optimal_threshold)])


if __name__ == "__main__":
    main()
