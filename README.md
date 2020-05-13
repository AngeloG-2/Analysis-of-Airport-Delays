The Goal of the Project
--------------------------
Determine the airpots with highest and lowest average delays.


The Dataset
--------------------------
The dataset is obtained from: https://www.kaggle.com/usdot/flight-delays

For this project, I will only be using the departure delay column and the airport column.

Number of columns: 5.82 MILLION 



Motivations of using csvreader rather than pandas
-------------------------
Given the size large size of the dataset (5.82 million rows) and the hardware limitations of my laptop, I chose to use csv module of python to read the data.

It turns that python's csvreader reads files increadibly fast and is memory efficient. Howwver, csv reader requires more coding unlike pandas.

When utilizing pandas for larger datasets, my memory ran out and it took 50 seconds to 70 seconds to read the file. While the implmentation with csv reader read the file, calculated summary statistics, and plotted histogram and 15 seconds max. 

The Results
--------------------------
Trenton-Mercer Airport had the highest average departure delay of 39.76 minutes with 34% of flights being delayed by 30 minutes or more. It can be seen that a large percentage of flights departing from Trenton-Mercer leave late. In fact, 47% of flights departing from Trenton-Mercer are delayed 10 minutes or more.

![TTN](TTN.PNG)





![Example Output](YAK.PNG)
