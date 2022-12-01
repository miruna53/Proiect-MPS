def f1(t1, t2, t3, optimal_threshold):
    return (t1 + t2 + t3) / 3


def f2(t1, t2, t3, optimal_threshold):
    dif1 = abs(t1 - optimal_threshold)
    dif2 = abs(t2 - optimal_threshold)
    dif3 = abs(t3 - optimal_threshold)

    return min(dif1, dif2, dif3)


def f3(t1, t2, t3, optimal_threshold):
    dif1 = abs(t1 - optimal_threshold)
    dif2 = abs(t2 - optimal_threshold)
    dif3 = abs(t3 - optimal_threshold)

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


def f4(t1, t2, t3, optimal_threshold):
    dif1 = abs(t1 - optimal_threshold)
    dif2 = abs(t2 - optimal_threshold)
    dif3 = abs(t3 - optimal_threshold)

    if dif1 == max(dif1, dif2, dif3):
        return (dif2 + dif3) / 2
    if dif2 == max(dif1, dif2, dif3):
        return (dif1 + dif3) / 2
    if dif3 == max(dif1, dif2, dif3):
        return (dif2 + dif1) / 2


def f5(t1, t2, t3, optimal_threshold):
    return (t1 * t2 * t3) ** (1./3.)
