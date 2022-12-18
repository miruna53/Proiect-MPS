import os
import glob
import csv
from local_file import *


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
            dictionary_row = dict(pixel_value = row[0], pixel_class = row[1], avg_th = row[2], midrange_th = row[3],
                              white_th = row[4], bernsen_th = row[5], niblack_th = row[6], sauvola_th = row[7],
                              wolf_th = row[8], phansalkar_th = row[9], nick_th = row[10], gaussian_th = row[11])
            list_per_file.append(dictionary_row)
        print(list_per_file)
    return local_file(list_per_file)
