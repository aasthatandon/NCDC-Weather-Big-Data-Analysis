# NCDC-Weather-Big-Data-Analysis


### Problem Statement :
Efficiently extract USAF weather station IDs and average wind direction, range of ceiling heights, and average visibility distances from the NCDC dataset to identify yearly trends.


### Project Description:
Performed comprehensive analysis on the National Climatic Data Center (NCDC) weather dataset, which comprises daily weather measurements (temperature, visibility distance, wind speed, humidity, pressure) from over 9000 weather stations worldwide, spanning the period from 1929 to 2020. For this project, I utilized both a university-managed Hadoop system on Unix and AWS, combining on-premises resources with cloud-based scalability.

### Data : 
Data is available under the folder ProjectData 

### Tools and Technologies:
MapReduce, Python, PySpark, Pig, Hive, AWS , HDFS

### Analysis and Insights:
•	Mapper and Reducer for Wind direction: Developed Mapper and Reducer to extract and calculate the average wind direction (degrees) for each observation month in NCDC records, grouped by year (e.g., 195001).<br>
•	PySpark Application for Sky Ceiling Heights: Created a PySpark application to efficiently determine the range (max-min) of sky ceiling heights (meters).<br>
•	Mapper and Reducer Implementation: Designed a custom Mapper and Reducer for extracting USAF weather station IDs and visibility distances from the NCDC dataset.<br>
•	Pig Data Analysis: Conducted data analysis using Pig to uncover annual visibility distance ranges, allowing for the identification of yearly trends.<br>
•	Hive Analytics: Leveraged Hive for computing the yearly average visibility distances, yielding valuable insights into long-term visibility patterns.<br>

### Files Overview :
#### Under Codes Folder
Mapper_part1.py : Mapper for extracting wind direction corresponding to each observation month in NCDC records, grouped by year.<br>
Reducer_part1.py : Reducer for calculating average wind direction from the input from Mapper_part1.py.<br>
PySpark_part2 : PySpark to determine the range (max-min) of sky ceiling heights (meters) for each USAF weather station ID.<br>
Mapper_part3.py : Mapper for extracting USAF weather station ID and visibility distance (meters) from NCDC records.<br>
Reducer_part3.py : Reducer for writing the USAF weather station ID and visibility distance data into a text file. <br>
visibility_data.txt :  Text file extracted after Reducer_part3.py which is utilized as an input for both pig and hive.<br>
#### Under Report Folder : 
Hive and Pig Programs: Refer part 4 in Bigdata_ProjectReport under Report folder.<br>
Bigdata_ProjectReport :  Walks through the entire process of this project step by step available under Report folder.



