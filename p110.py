import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()
print("population mean: ",statistics.mean(data))
def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(meanList):
    df = meanList
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    meanList = []
    for i in range(0,100):
        set_of_means= randomSetOfMean(30)
        meanList.append(set_of_means)
    show_fig(meanList)
    print("sampling mean:- ", statistics.mean(meanList))
setup()