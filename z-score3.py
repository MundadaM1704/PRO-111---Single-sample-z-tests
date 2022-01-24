import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import csv
import random

df = pd.read_csv("medium_data.csv")
reading_time = df["reading_time"].tolist()

def random_set_of_mean(counter):
    reading_timeset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(reading_time)-1)
        value = reading_time[random_index]
        reading_timeset.append(value)
    mean = statistics.mean(reading_timeset)
    return mean

# Function to get the mean of 30 reading_time sets
mean_list = []
for i in range(0,100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

## calculating mean and standard_deviation of the sampling distribution.
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)

## findig the standard deviation starting and ending values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
# print("std1",first_std_deviation_start, first_std_deviation_end)
# print("std2",second_std_deviation_start, second_std_deviation_end)
# print("std3",third_std_deviation_start,third_std_deviation_end)

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean_of_sample3 = statistics.mean(data)
print("Mean of sample3:- ",mean_of_sample3)
fig = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF READING TIME"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

#finding the z score using the formula
z_score3 = (mean - mean_of_sample3)/std_deviation
print("The z score of sample 3 is = ",z_score3)
