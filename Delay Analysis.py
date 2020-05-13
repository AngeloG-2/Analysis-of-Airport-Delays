# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:28:44 2020

@author: Angelo Gaerlan
"""

import pandas as pd
import csv
import statistics 
import matplotlib.pyplot as plt


def groupby_delays():
    '''
    
    GIVEN A TABLE:
    
    flight_number    airport     departure_delay (minutes)
    2947             LAX         -8
    123              LAX         17
    3716             SFO         28
    3927             YVR         9
    1233             SFO         21
    
    THE FUNCTION WILL RETURN A DICTIONARY WITH AIRPORT AS THE KEY AND A LIST OF CORRESPONDING FLIGHT DELAYS
    
    THE FUNCTION WILL RETURN A DICTIONARY THAT LOOKS LIKE:
    
    {'LAX':[-8, 17], 'SFO':[28, 21], 'YVR':[9]}
    
    '''
    
    data_dict = {}

    with open("flights_original.csv", "r") as files:       
        reader = csv.reader(files)
        next(reader, None)
   
        for data in reader:
            airport_code = data[7]
            depart_delay = data[11]
            if depart_delay != '':
                if (airport_code in data_dict):
                    data_dict[airport_code].append(float(depart_delay))
                elif not(airport_code in data_dict):
                    data_dict[airport_code] = [float(depart_delay)]
    
    return data_dict


def calculate_statistics(data_dict):
    
    '''
    
    USING THE DATA DICTIONARY FROM THE groupby_delays(), THE FUNCTION WILL CALCULATE
    SUMMARY STATISTICS ON THE DELAY DATA FOR EACH AIRPORT. the INDIVIDUAL AIRPORT DATA WILL BE 
    STORED AS A LIST OF TUPLES, WHERE EACH TUPLE CONTAINS THE AIRPOT NAME AND THE CORRESPONDING SUMMARY STATISTICS.
    
    SUMMARY STATISTICS CALCULATED:
        
    1. Average delay
    2. Standard Deviation of delays
    3. Max delay
    4. Min delay
    
    THE FUNCTION WILL RETURN A LIST THAT LOOKS LIKE:
    
    [ ('LAX', 2.7, 287, 87, 2, 3927), ('SFO', 4.8, 2.7, 55, 27, 93817), ('YVR', 15.6, 28.47, 40, 7, 2918) ] 
    
    '''
    
    airport_data = []
    
    for airport in data_dict:
        delay_data = data_dict[airport]
        average_delay = round(statistics.mean(delay_data),2)
        delay_stddev = round(statistics.pstdev(delay_data),2)
        max_delay = int(max(delay_data))
        min_delay = int(min(delay_data))
        flight_count = int(len(delay_data))
        
        airport_data.append((airport,average_delay,delay_stddev,max_delay,min_delay,flight_count))
        
    return airport_data
        


def convert_to_dataframe(airport_data):
    
    '''
    
    GIVEN THE LIST OF TUPLES CALCULATED FROM calculate_statistics(), THE FUNCTION WILL CONVERT THE LIST OF TUPLES
    TO a pandas DataFrame.
    
    THE FUNCTION WILL ALSO SAVE THE DATAFRAME INTO A CSV.
    
    
    '''
    
    df = pd.DataFrame(airport_data, columns=['airport', 'avg_delay','delay_stddev','max_delay','min_delay', 'num_fligts'])
    
    df.to_csv('flights_aNalyzed.csv')
    
    return df
    


def plot_histogram(data_arr, airport_code):
    
    '''
    GIVEN A DELAY DATA OF A SPECIFIC AIRPORT, AND THE AIRPORT CODE, THE FUNCTION WILL CREATE A HISTOGRAM OF THE AIRPORT DELAYS.
    
    '''
    
    
    plt.hist(data_arr, color = 'blue', edgecolor = 'black',bins = int(40), range=[min(data_arr),170] )
    plt.axvline(statistics.mean(data_arr), color='k', linestyle='dashed', linewidth=2)
    plt.axvline(0, color='red', linestyle='dashed', linewidth=2)
    plt.title('Histogram of Departure Delays at {}'.format(airport_code))
    plt.xlabel('Departure Delay (minutes)')
    _, max_ = plt.ylim()
    plt.text(statistics.mean(data_arr) + statistics.mean(data_arr)/10, max_ - max_/10, 'Mean: {:.2f}'.format(statistics.mean(data_arr)))
    plt.text(0, max_ - max_/5, '0 Delay')
    plt.ylabel('Frequency')
    plt.savefig('{}.png'.format(airport_code))
    plt.show()





'''
CREATES A TABLE OF SUMMARY STATTISTICS OF AIRPORT DELAYS AND SAVES IT AS A CSV
'''
print(convert_to_dataframe(calculate_statistics(groupby_delays())))


'''
CREATES A HISTOGRAM OF AVERAGE DELAYS OF A GIVEN AIRPROT
'''
airport = 'TTN'
plot_histogram(groupby_delays()[airport],airport)


        
            
            







