import pandas as pd

def load_data(path, features):
    df = pd.read_csv(path)
    data = df.to_dict("list")
    return data

def print_details(data, features, statistic_functions):
    for feature in features:
        if feature in data.keys():
            formatted_mean = "{:.2f}".format(statistic_functions[0](data[feature]))
            formatted_stdv = "{:.2f}".format(statistic_functions[1](data[feature]))
            print( f"{feature}: {formatted_mean}, {formatted_stdv}")

def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    for func, func_name in zip(statistic_functions, statistic_functions_names):
        stat_data = func(data[features[0]], data[features[1]])
        formatted_data = "{:.2f}".format(stat_data)
        print(f"{func_name}({features[0]}, {features[1]}): {formatted_data}")

def filter_by_feature(data, feature, values):
    all_values = data[feature]
    good_indexes = []
    data1 = {}
    data2 = {}

    for index, val in enumerate(all_values):
        if all_values[index] in values:
            good_indexes.append(index)

    for key in data.keys():
        data1[key] = []
        data2[key] = []
        for index, item in enumerate(data[key]):
            if index in good_indexes:
                data1[key].append(data[key][index])
            else:
                data2[key].append(data[key][index])

    return data1, data2

