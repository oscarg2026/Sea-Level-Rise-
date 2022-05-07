import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig , ax = plt.subplots()
    ax = plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lin1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax = plt.plot(df['Year'], lin1.slope*df['Year']+lin1.intercept)

    # Create second line of best fit
    ax = plt.plot(np.arange(2000,2050), lin1.slope*np.arange(2000,2050)+lin1.intercept)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()