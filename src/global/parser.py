import pandas as pd
import numpy as np
import os
import glob
import csv
from file import *
def getFiles():
    path = os.getcwd()
    path += '\..\..\data\global-data'
    print(path)

    return glob.glob(os.path.join(path, "*.csv"))

def convert(string):
    li = string.split(",")

    while ("" in li):
        li.remove("")

    return li

def parseFile(file):
    optimal_threshold = 0
    #thresholds = []
    #f_measures = []

    with open(file, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            if i == 0:
                thresholds = [float(num) for num in convert(line[0])]
                optimal_threshold = thresholds[0]
                thresholds = thresholds[1:]
                print("Thresholds: ", thresholds, '\n')
            if i == 1:
                f_measures = [float(num) for num in convert(line[0])]
                print("F-measures: ", f_measures, '\n')

    print("Optimal threshold: ", optimal_threshold)

    return File(thresholds, optimal_threshold, f_measures)

# print(len(getFiles()))
# for file in getFiles():
#     parseFile(file)
