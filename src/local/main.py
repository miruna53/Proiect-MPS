from csv_local_parser import *
from LocalFile import *


def main():
    files = []
    csv_files = get_files()
    for csv_file in csv_files[0:1]:
        files.append(parse_file(csv_file))

    print(files[0].get_pixel_list()[0].get_thresholds())


if __name__ == "__main__":
    main()
