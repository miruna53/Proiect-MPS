import math


def f1(t1, t2):
    return (t1 + t2) / 2


def f2(t1, t2):
    return (t1 * t2) ** (1./2.)


def f3(t1, t2):
    return min(t1, t2)


def f4(t1, t2):
    return max(t1, t2)


def f5(t1, t2):
    return 0.4 * t1 + 0.6 * t2


def root1(t1, t2, t3, t4, t5):
        return (t1 + t2 + t3 + t4 + t5) / 5


def root2(t1, t2, t3, t4, t5):
    return (t1 * t2 * t3 * t4 * t5) ** (1./5.)
