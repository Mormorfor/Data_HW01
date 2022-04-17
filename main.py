import sys
import data
import statistics

def main(argv):
    path = "//home//student//Homeworks//HW01//london_sample.csv"
    features = "hum, t1, cnt, season, is_holiday"
 #   path = argv[1]
 #   features = argv[2]
 #   data.load_data(path, features)
    li =  [0]
    dt = data.load_data(path,features)
  #  data.filter_by_feature(dt ,"is_holiday", li)

  #  statistics.calc_stdv([1,2,4,5,6,10])
  #  statistics.calc_covariance([1,2,4,5,6,10], [1,5,8,8,10,3])
    statistic_functions = [statistics.calc_mean,statistics.calc_stdv, statistics.calc_covariance]
    winter_data = data.filter_by_feature(dt,"season",[3])
    is_hol = [1]
    winter_holiday_data = data.filter_by_feature(winter_data[0],"is_holiday",is_hol)
    statistics.population_statistics("Winter", winter_holiday_data[0], "t1", "cnt", 13.0, True, statistic_functions)

if __name__ == '__main__':
    main(sys.argv)


