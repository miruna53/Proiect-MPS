import os
import glob
import csv
from LocalFile import *
from Pixel import *


def get_files():
    path = os.getcwd()
    path += '\..\..\data\local-data'
    print(path)

    return glob.glob(os.path.join(path, "*.csv"))


def parse_file(file):
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        list_per_file = []
        for row in reader:
            pixel = Pixel(float(row[0]), float(row[1]), [eval(i) for i in row[2:11]])
            list_per_file.append(pixel)

    return LocalFile(list_per_file)
