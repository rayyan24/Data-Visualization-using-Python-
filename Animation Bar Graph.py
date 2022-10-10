import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from time import sleep



covidData = pd.read_csv("Dataset.csv")
dates = covidData["Date"].unique()
# sub plot function returns a figure and axis objects
figure, axis = plt.subplots(figsize=(15, 8))
countries = ["India", "China", "US", "Italy", "Spain"]
colors = ["black", 'red', "green", 'blue', "yellow"]


def animFunc(Date):
    dateDF = covidData[covidData["Date"].eq(Date)]
    axis.clear()
    deathsDF=dateDF.sort_values(by='Deaths',ascending=0)
    countryDF=deathsDF[deathsDF['Country'].isin(countries)]
    sleep(0.2)
    return axis.barh(countryDF['Country'],countryDF['Deaths'],color=colors)
# frames is the animation on which animation is to be done
# blit increase quality of animation
Animation=anim.FuncAnimation(fig=figure,func=animFunc,frames=dates,blit=1,interval=20)
plt.show()