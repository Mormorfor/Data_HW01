import pandas as pd

def load_data(path, features):
    df = pd.read_csv(path)
    data = df.to_dict("list")
    return data

def print_details(data, features, statistic_functions):
    pass


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

