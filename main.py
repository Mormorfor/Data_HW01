import sys
import data
import statistics

def main(argv):
    path = "//home//student//Homeworks//HW01//london_sample.csv"
    features = "hum, t1, cnt, season, is_holiday"
 #   path = argv[1]
 #   features = argv[2]
 #   data.load_data(path, features)

    dt = data.load_data(path,features)
    statistic_functions = [statistics.calc_mean, statistics.calc_stdv]
    joined_stat_functions = [statistics.calc_covariance]

    print("Question 1:")
    data_selections = {"Summer" : data.filter_by_feature(dt,"season",[1])[0], "Holiday" : data.filter_by_feature(dt,"is_holiday",[1])[0],
            "All" : dt}
    features = ["hum", "t1", "cnt"]
    cov_features = ["t1", "cnt"]
    names_cov_features = ["Cov"]

    for key in data_selections.keys():
        print(f"{key}:")
        data.print_details(data_selections[key], features, statistic_functions)
        data.print_joint_details(data_selections[key], cov_features, joined_stat_functions, names_cov_features)



    print()
    print("Question 2:")

    winter_data = data.filter_by_feature(dt, "season", [3])
    winter_holiday_data = data.filter_by_feature(winter_data[0], "is_holiday", [1])
    threshold = 13.0
    is_above = False

    print(f"If t1<={threshold}, then:")
    statistics.population_statistics("Winter Holiday records", winter_holiday_data[0], "t1", "cnt",
                                     threshold, is_above, statistic_functions)
    statistics.population_statistics("Winter Weekday records", winter_holiday_data[1], "t1", "cnt",
                                     threshold, is_above, statistic_functions)
    print(f"If t1>{threshold}, then:")
    is_above = True
    statistics.population_statistics("Winter Holiday records", winter_holiday_data[0], "t1", "cnt",
                                     threshold, is_above, statistic_functions)
    statistics.population_statistics("Winter Weekday records", winter_holiday_data[1], "t1", "cnt",
                                     threshold, is_above, statistic_functions)



if __name__ == '__main__':
    main(sys.argv)


