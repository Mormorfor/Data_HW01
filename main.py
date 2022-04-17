import sys
import data


def main(argv):
    path = "//home//student//Homeworks//HW01//london_sample.csv"
    features = "hum, t1, cnt, season, is_holiday"
 #   path = argv[1]
 #   features = argv[2]
 #   data.load_data(path, features)
    li =  [0]
    dt = data.load_data(path,features)
    data.filter_by_feature(dt ,"is_holiday", li )
if __name__ == '__main__':
    main(sys.argv)


