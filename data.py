import pandas as pd

def load_data(path, features):
    df = pd.read_csv(path)
    data = df.to_dict("list")
    return data


def filter_by_feature(data, feature, values):
    all_values = data[feature]
    #print(all_values)
    good_indexes = []
    bad_indexes = []
    data1 = {}
    data2 = {}

    for index, val in enumerate(all_values):
        if all_values[index] in values:
        #    print(val, index)
            good_indexes.append(index)
        else:
        #    print(index, val)
            bad_indexes.append(index)

    for key in data.keys():
       # print(key)
        data1[key] = []
        data2[key] = []
       # print(data1.items())
       # print(data1.keys())
        for index, item in enumerate(data[key]):
            if index in good_indexes:
                #print(data[key][index])
                data1[key].append(data[key][index])

        for index, item in enumerate(data[key]):
            if index in bad_indexes:
                #print(data[key][index])
                data2[key].append(data[key][index])

    #print(data1.items())
    #print(data2.items())
    return data1, data2


def filter_by_feature_old(data, feature, values):
    list_of_values = data[feature]
    print(list_of_values)
    good_indexes = []
    bad_indexes = []
    data1 = {}
    data2 = {}
    for i in list_of_values:
        if list_of_values[i] in values:
            good_indexes.append(i)
        else:
            bad_indexes.append(i)

    for key in data.keys():
        for j in data[key]:
            if j in good_indexes:
                data1[key].append(data[key][j])

    for key in data.keys():
        for j in data[key]:
            if j in bad_indexes:
                data2[key].append(data[key][j])

    print(data1.keys())
    print(data2.keys())