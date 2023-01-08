import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from forex_python.converter import CurrencyRates

cr = CurrencyRates()

'''
Showcase of data analysis using numpy, pandas, forex, and matplotlib
for a dataset sourced @ https://www.kaggle.com/datasets/mvieira101/global-cost-of-living
global cost of living for 4956 cities around the world.
Data updated from December 2022

by Holly DuCoing
'''

datasetFile = 'global_cost_of_living_dataset/cost-of-living_v2.csv'
data = pd.read_csv(datasetFile)


def WaterCosts(data):
    # x8 = water costs in USD
    df = pd.DataFrame(data, columns=['country', 'city', 'x8'])
    nzIndexes = np.where(df.loc[0:] == 'New Zealand')
    nzIndexes = [i for i in nzIndexes[0]]

    nzWaterData = []
    for i in nzIndexes:
        nzWaterData.append(df.loc[i])

    ydata = []
    xdata = []
    for j in nzWaterData:
        # Pulls live conversion rate of usd to nzd and converts it (is slightly lower than putting in rate manually)
        ydata.append(j[2]*cr.get_rate('USD','NZD'))
        xdata.append(j[1])
    # plots x and y data into horizontal bar chart
    plt.barh(xdata,ydata, color="PaleTurquoise")
    plt.xlabel("NZD")
    plt.title("Average Cost of Water in New Zealand Cities")
    plt.show()

WaterCosts(data)
def CoffeeCosts(data):
    # x6 = cappuccino costs in usd
    df = pd.DataFrame(data, columns=['country', 'city', 'x6'])
    nzIndexes = np.where(df.loc[0:] == 'New Zealand')
    nzIndexes = [i for i in nzIndexes[0]]

    nzCapData = []
    for i in nzIndexes:
        nzCapData.append(df.loc[i])
    ydata = []
    xdata = []
    for j in nzCapData:
        # Pulls live conversion rate of usd to nzd and converts it (is slightly lower than putting in rate manually)
        ydata.append(j[2] * cr.get_rate('USD', 'NZD'))
        xdata.append(j[1])
        # plots x and y data into horizontal bar chart
    plt.barh(xdata, ydata, color="SaddleBrown")
    plt.xlabel("NZD")
    plt.title("Average Cost of Cappuccinos in New Zealand")
    plt.show()

CoffeeCosts(data)

def ApartmentCosts(data):
    # x52 = apartment in city centre to buy - per square metre costs in USD
    df = pd.DataFrame(data, columns=['country', 'city', 'x52'])
    nzIndexes = np.where(df.loc[0:] == 'New Zealand')
    nzIndexes = [i for i in nzIndexes[0]]

    nzAptData = []
    for i in nzIndexes:
        nzAptData.append(df.loc[i])
    ydata = []
    xdata = []
    for j in nzAptData:
        # Pulls live conversion rate of usd to nzd and converts it (is slightly lower than putting in rate manually)
        ydata.append(j[2] * cr.get_rate('USD', 'NZD'))
        xdata.append(j[1])
        # plots x and y data into horizontal bar chart
    plt.barh(xdata, ydata, color="NavajoWhite")
    plt.xlabel("NZD")
    plt.title("Average Cost of Buying an Apartment in New Zealand Cities")
    plt.show()

ApartmentCosts(data)

def MealCosts(data):
    # x1 meal at inexpensive resturaunt in USD
    df = pd.DataFrame(data, columns=['country', 'city', 'x1'])
    nzIndexes = np.where(df.loc[0:] == 'New Zealand')
    nzIndexes = [i for i in nzIndexes[0]]

    nzMealData = []
    for i in nzIndexes:
        nzMealData.append(df.loc[i])
    ydata = []
    xdata = []
    for j in nzMealData:
        # Pulls live conversion rate of usd to nzd and converts it (is slightly lower than putting in rate manually)
        ydata.append(j[2] * cr.get_rate('USD', 'NZD'))
        xdata.append(j[1])
        # plots x and y data into horizontal bar chart
    plt.barh(xdata, ydata, color="Salmon")
    plt.xlabel("NZD")
    plt.title("Average Cost of Meal at Inexpensive Resturaunt in New Zealand")
    plt.show()

MealCosts(data)