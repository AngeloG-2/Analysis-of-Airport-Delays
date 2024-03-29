The Goal of the Project
--------------------------
1. Determine the airpots with highest and lowest average delays

2. Determine the relationship between the average delay of an airport and the number of flights.


The Dataset
--------------------------
The dataset is obtained from: https://www.kaggle.com/usdot/flight-delays

For this project, I will only be using the departure delay column and the airport column.

Number of rows: 5.82 MILLION 



Motivations of using csvreader rather than pandas
-------------------------
Given the size large size of the dataset (5.82 million rows) and the hardware limitations of my laptop, I chose to use csv module of python to read the data.

It turns that python's csvreader reads files incredibly fast and is memory efficient. However, csv reader requires more coding, unlike pandas.

When utilizing pandas for larger datasets, my memory ran out, and it took 50 seconds to 70 seconds to read the file. While the implementation with csv reader read the file, calculated summary statistics, and plotted histogram in 10 - 15 seconds max. 

pandas is an incredibly powerful library that provides convenient functionality when working with data; however, my laptop is too slow to utilize the library with large datasets.

The Results
--------------------------
Trenton-Mercer Airport (TTN) had the highest average departure delay of 39.76 minutes with 34% of flights being delayed by 30 minutes or more. It can be seen that a large percentage of flights departing from Trenton-Mercer leave late. In fact, 47% of flights departing from Trenton-Mercer are delayed 10 minutes or more.

![image](https://user-images.githubusercontent.com/40840760/150709887-0b95b297-6211-4745-9cab-3a88fe69264e.png)



Yakutat Airport (YAK) had the lowest average departure delay of -8.77 minutes with only 6.8% of flights being delayed by 30 minutes or more. It can be seen that a large percentage of flights out of Yakutat airport leave on time. In fact, 84.06% of departing flights out of Yakutat leave early or depart on time. This explains the negative average departure delay.

![image](https://user-images.githubusercontent.com/40840760/150709971-cbf3d546-a166-4909-ac11-b0633eb3fee3.png)


The Pearson’s correlation coefficient is 0.0698 suggesting a very-weak positive correlation between the number of flights per year and the average delay. This suggests that the busyness of an airport does not affect the average delay in an airport. If look at airports with less than 8000 flights, we see a wide range of average delays. Average departure delay may depend on how effective airports scale their operations with increasing number of flights and passengers.

![image](https://user-images.githubusercontent.com/40840760/150710018-a2c54f74-a51d-402c-a12e-5d5e1b69a34f.png)

