The Goal of the Project
--------------------------
1. Determine the airpots with highest and lowest average delays

2. Determine the relationship between the average delay of an airport and the number of flights.


The Dataset
--------------------------
The dataset is obtained from: https://www.kaggle.com/usdot/flight-delays

For this project, I will only be using the departure delay column and the airport column.

Number of columns: 5.82 MILLION 



Motivations of using csvreader rather than pandas
-------------------------
Given the size large size of the dataset (5.82 million rows) and the hardware limitations of my laptop, I chose to use csv module of python to read the data.

It turns that python's csvreader reads files increadibly fast and is memory efficient. Howwver, csv reader requires more coding unlike pandas.

When utilizing pandas for larger datasets, my memory ran out and it took 50 seconds to 70 seconds to read the file. While the implmentation with csv reader read the file, calculated summary statistics, and plotted histogram in 10 - 15 seconds max. 

pandas is an incredibly powerful library that provides convinient functionality when working with data; howver, my laptop is too slow to utilize the library with large datasets.

The Results
--------------------------
Trenton-Mercer Airport had the highest average departure delay of 39.76 minutes with 34% of flights being delayed by 30 minutes or more. It can be seen that a large percentage of flights departing from Trenton-Mercer leave late. In fact, 47% of flights departing from Trenton-Mercer are delayed 10 minutes or more.
![TTN](TTN.PNG)



Yakutat Airport had the lowest average departure delay of -8.77 minutes with only 6.8% of flights being delayed by 30 minutes or more. It can be seen that a large percentage of flights out of Yakutat airport leave on time. In fact, 84.06% of departing flights out of Yakutat leave early or depart on time. This explains the negative average departure delay.
![YAK](YAK.PNG)


The Pearson’s correlation coefficient is 0.0698 suggesting a very-weak positive correlation between the number of flights per year and the average delay. This suggests that the busyness of an airport does not affect the average delay in an airport. If look at airports with less than 8000 flights, we see a wide range of average delays. Average departure delay may depend on how effective airports scale their operations with increasing number of flights and passengers.
