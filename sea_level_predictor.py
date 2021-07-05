import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, axes = plt.subplots(figsize=(10, 10))
    plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)
    #plt.show()
    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    #print(res)
    x = df["Year"].append(pd.Series(range(2014, 2051)))
    #print(x)
    y = res.slope * x + res.intercept
    plt.plot(x, y, "g")
    # Create second line of best fit
    res2 = linregress(df[df['Year'] >= 2000]["Year"], df[df['Year'] >= 2000]["CSIRO Adjusted Sea Level"])
    #print(res2)
    x2 = pd.Series(range(2000, 2051))
    #print(x)
    y2 = res2.slope * x2 + res2.intercept
    plt.plot(x2, y2, "r")
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()