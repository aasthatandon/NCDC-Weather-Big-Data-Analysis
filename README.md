# NCDC-Weather-Big-Data-Analysis


Problem Statement :
Efficiently extract USAF weather station IDs and average wind direction, range of ceiling heights, and average visibility distances from the NCDC dataset to identify yearly trends.


Project Description:
Performed comprehensive analysis on the National Climatic Data Center (NCDC) weather dataset, which comprises daily weather measurements (temperature, visibility distance, wind speed, humidity, pressure) from over 9000 weather stations worldwide, spanning the period from 1929 to 2020. For this project, I utilized both a university-managed Hadoop system on Unix and AWS, combining on-premises resources with cloud-based scalability.


Tools and Technologies: 
MapReduce, Python, PySpark, Pig, Hive, AWS , HDFS


Analysis and Insights:
•	Mapper and Reducer for Wind direction: Developed Mapper and Reducer to extract and calculate the average wind direction (degrees) for each observation month in NCDC records, grouped by year (e.g., 195001).
•	PySpark Application for Sky Ceiling Heights: Created a PySpark application to efficiently determine the range (max-min) of sky ceiling heights (meters).
•	Mapper and Reducer Implementation: Designed a custom Mapper and Reducer for extracting USAF weather station IDs and visibility distances from the NCDC dataset.
•	Pig Data Analysis: Conducted data analysis using Pig to uncover annual visibility distance ranges, allowing for the identification of yearly trends.
•	Hive Analytics: Leveraged Hive for computing the yearly average visibility distances, yielding valuable insights into long-term visibility patterns

