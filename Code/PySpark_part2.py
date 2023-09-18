from pyspark import SparkContext

def main():
    #Create a sparkcontext
    sc = SparkContext(appName='RangeSkyceilingbyWeatherstation')

    # Import the input file
    input_rdd = sc.textFile('/user/hadoop/BAN632Project/ProjectData/')

    # filter out records with invalid quantity values and sky ceiling height
    filtered_rdd = input_rdd.filter(lambda line: line[70:75] != "99999" and int(line[75:76]) in [0,1,4,5,9])

    # extract the USAF weather station ID and sky ceiling height and convert them into pairs
    usaf_rdd = filtered_rdd.map(lambda line: (line[4:10], int(line[70:75])))

    # calculate the the range of sky ceiling height (meters) for each USAF weather station ID
    skyrange_rdd = usaf_rdd.groupByKey().mapValues(lambda values: max(values) - min(values))

    # save the output to a final output file
    skyrange_rdd.saveAsTextFile('/user/hadoop/outputpart2')
    sc.stop()
    
if __name__ == '__main__':
    main()