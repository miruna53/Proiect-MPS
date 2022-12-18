from csv_local_parser import *
from local_file import *

def main():
    files = []

    for csv_file in get_files():
        files.append(parse_file(csv_file))

    print(files)

if __name__ == "__main__":
    main()
