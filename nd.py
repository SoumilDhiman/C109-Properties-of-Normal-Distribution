import random
import plotly.express as pe
import plotly.figure_factory as pf
import statistics
import plotly.graph_objects as pg
import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()
#mean
mean = sum(data)/len(data)
st = statistics.stdev(data)
#median
median = statistics.median(data)
#mode
mode = statistics.mode(data)
print("Mean: ",mean,"Median: ",median,"Mode: ",mode)
#finding 1sd start and end value and 2sd start and end value
sd1Start,sd1End = mean-st,mean+st
sd2Start,sd2End = mean-(2*st),mean+(2*st)
sd3Start,sd3End = mean-(3*st),mean+(3*st)
sd1Data = [result1 for result1 in data if result1>sd1Start and result1<sd1End]
sd2Data = [result1 for result1 in data if result1>sd2Start and result1<sd2End]
sd3Data = [result1 for result1 in data if result1>sd3Start and result1<sd3End]
print("{}% Data Lies Within sd1". format(len(sd1Data)*100.0/len(data)))
print("{}% Data Lies Within sd2". format(len(sd2Data)*100.0/len(data)))
print("{}% Data Lies Within sd3". format(len(sd3Data)*100.0/len(data)))
fig = pf.create_distplot([data],["Result"],show_hist=False)
fig.add_trace(pg.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "Mean"))
fig.add_trace(pg.Scatter(x = [sd1Start,sd1Start],y = [0,0.17],mode = "lines",name = "SD1"))
fig.add_trace(pg.Scatter(x = [sd1End,sd1End],y = [0,0.17],mode = "lines",name = "SD1"))
fig.add_trace(pg.Scatter(x = [sd2Start,sd2Start],y = [0,0.17],mode = "lines",name = "SD2"))
fig.add_trace(pg.Scatter(x = [sd2End,sd2End],y = [0,0.17],mode = "lines",name = "SD2"))
fig.add_trace(pg.Scatter(x = [sd3Start,sd3Start],y = [0,0.17],mode = "lines",name = "SD3"))
fig.add_trace(pg.Scatter(x = [sd3End,sd3End],y = [0,0.17],mode = "lines",name = "SD2"))
fig.show()