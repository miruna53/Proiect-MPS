import math


def f1(t1, t2, t3, optimal_threshold, f_measures):
    return (t1 + t2 + t3) / 3


def f2(t1, t2, t3, optimal_threshold, f_measures):
    dif1 = abs(f_measures[math.floor(t1 * 255)] - f_measures[math.floor(optimal_threshold * 255)])
    dif2 = abs(f_measures[math.floor(t2 * 255)] - f_measures[math.floor(optimal_threshold * 255)])
    dif3 = abs(f_measures[math.floor(t3 * 255)] - f_measures[math.floor(optimal_threshold * 255)])

    if dif1 == min(dif1, dif2, dif3):
        return t1
    if dif2 == min(dif1, dif2, dif3):
        return t2
    if dif3 == min(dif1, dif2, dif3):
        return t3


def f3(t1, t2, t3, optimal_threshold, f_measures):
    dif1 = abs(f_measures[math.floor(t1 * 255)] - f_measures[math.floor(optimal_threshold * 255)])
    dif2 = abs(f_measures[math.floor(t2 * 255)] - f_measures[math.floor(optimal_threshold * 255)])
    dif3 = abs(f_measures[math.floor(t3 * 255)] - f_measures[math.floor(optimal_threshold * 255)])

    if dif1 == min(dif1, dif2, dif3):
        if dif2 == min(dif2, dif3):
            return 0.7 * t1 + 0.2 * t2 + 0.1 * t3
        else:
            return 0.7 * t1 + 0.2 * t3 + 0.1 * t2

    if dif2 == min(dif1, dif2, dif3):
        if dif1 == min(dif1, dif3):
            return 0.7 * t2 + 0.2 * t1 + 0.1 * t3
        else:
            return 0.7 * t2 + 0.2 * t3 + 0.1 * t1

    if dif3 == min(dif1, dif2, dif3):
        if dif1 == min(dif1, dif2):
            return 0.7 * t3 + 0.2 * t1 + 0.1 * t2
        else:
            return 0.7 * t3 + 0.2 * t2 + 0.1 * t1


def f4(t1, t2, t3, optimal_threshold, f_measures):
    dif1 = abs(f_measures[math.floor(t1 * 255)] - f_measures[math.floor(optimal_threshold * 255)])
    dif2 = abs(f_measures[math.floor(t2 * 255)] - f_measures[math.floor(optimal_threshold * 255)])
    dif3 = abs(f_measures[math.floor(t3 * 255)] - f_measures[math.floor(optimal_threshold * 255)])

    if dif1 == max(dif1, dif2, dif3):
        return (t2 + t3) / 2
    if dif2 == max(dif1, dif2, dif3):
        return (t1 + t3) / 2
    if dif3 == max(dif1, dif2, dif3):
        return (t2 + t1) / 2


def f5(t1, t2, t3, optimal_threshold, f_measures):
    return (t1 * t2 * t3) ** (1./3.)


def root1(t1, t2, t3, t4, t5, optimal_threshold, f_measures):
    return (t1 + t2 + t3 + t4 + t5) / 5


def root2(t1, t2, t3, t4, t5, optimal_threshold, f_measures):
    return (t1 * t2 * t3 * t4 * t5) ** (1./5.)