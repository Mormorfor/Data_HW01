from math import sqrt
import data as dt

def calc_mean(values):
    return sum(values) / len(values)

def calc_stdv(values):
    mean = calc_mean(values)
    sq_sum = 0
    for val in values:
        element = (val - mean)
        sq_sum += (element ** 2)
    result = sqrt(sq_sum / (len(values)-1))
    return result

def calc_covariance(values1, values2):
    mean_x = calc_mean(values1)
    mean_y = calc_mean(values2)
    element = 0
    for val_x, val_y in zip(values1, values2):
        element += (val_x - mean_x)*(val_y - mean_y)
    result = element / (len(values1) - 1)
    return result

def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    print(f"{feature_description}:")
    values_above_threshold = []

    for val in data[treatment]:
        if val > threshold:
            values_above_threshold.append(val)

    filtered_data = dt.filter_by_feature(data, treatment, values_above_threshold)
    if(is_above):
        formatted_mean = "{:.2f}".format(statistic_functions[0](filtered_data[0][target]))
        formatted_stdv = "{:.2f}".format(statistic_functions[1](filtered_data[0][target]))
        print(f"{target}: {formatted_mean}, {formatted_stdv}")
    else:
        formatted_mean = "{:.2f}".format(statistic_functions[0](filtered_data[1][target]))
        formatted_stdv = "{:.2f}".format(statistic_functions[1](filtered_data[1][target]))
        print( f"{target}: {formatted_mean}, {formatted_stdv}")




