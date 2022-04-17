from math import sqrt
import data

def calc_mean(values):
    return round(sum(values) / len(values), 2)

def calc_stdv(values):
    mean = calc_mean(values)
    sq_sum = 0
    for val in values:
        element = (val - mean)
        sq_sum += (element ** 2)
    result = sqrt(sq_sum / (len(values)-1))
    print(result)
    return round(result, 2)

def calc_covariance(values1, values2):
    mean_x = calc_mean(values1)
    mean_y = calc_mean(values2)
    print(mean_x, mean_y)
    element = 0
    for val_x, val_y in zip(values1, values2):
        element += (val_x - mean_x)*(val_y - mean_y)
    result = element / (len(values1) - 1)
    print(result)
    return round(result, 2)

def population_statistics(feature_description, input_data, treatment, target, threshold, is_above, statistic_functions):
    print(feature_description)
    values_above_threshold = []

    for val in input_data[treatment]:
        if val > threshold:
            values_above_threshold.append(val)

    filtered_data = data.filter_by_feature(input_data, treatment, values_above_threshold)
    if(is_above):
        print(f"{target}: {statistic_functions[0](filtered_data[0][target])}, {statistic_functions[1](filtered_data[0][target])}")
    else:
        print(
            f"{target}: {statistic_functions[0](filtered_data[1][target])}, {statistic_functions[1](filtered_data[1][target])}")




