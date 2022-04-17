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

    statistic_functions = [statistics.calc_mean,statistics.calc_stdv]
    joined_stat_functions = [statistics.calc_covariance]

    summer_data = data.filter_by_feature(dt,"season",[1])
    features = ["hum", "t1", "cnt"]
    cov_features = ["t1", "cnt"]
    names_cov_features = ["Cov"]

    data.print_details(summer_data[0], features, statistic_functions)
    data.print_joint_details(summer_data[0],cov_features,joined_stat_functions, names_cov_features)


    winter_data = data.filter_by_feature(dt,"season",[3])
    winter_holiday_data = data.filter_by_feature(winter_data[0],"is_holiday",[1])

    statistics.population_statistics("Winter Holiday records", winter_holiday_data[0], "t1", "cnt",
                                     13.0, True, statistic_functions)
    statistics.population_statistics("Winter Weekday records", winter_holiday_data[1], "t1", "cnt",
                                     13.0, True, statistic_functions)



if __name__ == '__main__':
    main(sys.argv)


