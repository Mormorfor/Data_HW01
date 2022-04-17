from math import sqrt


def calc_mean(values):
    return sum(values) / len(values)

def calc_stdv(values):
    mean = calc_mean(values)
    sq_sum = 0
    for val in values:
        element = (val - mean)
        sq_sum += (element ** 2)
    result = sqrt(sq_sum / (len(values)-1))
    print(result)
    return result

def calc_covariance(values1, values2):
    mean_x = calc_mean(values1)
    mean_y = calc_mean(values2)
    print(mean_x, mean_y)
    element = 0
    for val_x, val_y in zip(values1, values2):
        element += (val_x - mean_x)*(val_y - mean_y)
    result = element / (len(values1) - 1)
    print(result)
    return result

def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    pass