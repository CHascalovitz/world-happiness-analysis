import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import csv

# Load data
dataframe = pd.read_csv('./data/WHR_2019_Full.csv')

dataframe = dataframe.dropna(subset=['Overall rank', 'Continent', 'Country or region', 'Score', 'GDP per capita', 'Social support',
'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption',
'Gini index'])

overall = dataframe['Overall rank'].values
continent = dataframe['Continent'].values
country = dataframe['Country or region'].values
score = dataframe['Score'].values
gdp = dataframe['GDP per capita'].values
social = dataframe['Social support'].values
lifestyle = dataframe['Healthy life expectancy'].values
freedom = dataframe['Freedom to make life choices'].values
generosity = dataframe['Generosity'].values
perception = dataframe['Perceptions of corruption'].values
gini = dataframe['Gini index'].values

# Create colour scheme
color_map = {
1: (1, 0.7849031270994535, 0.775031116112941),
2: (1, 0.3847458156188478, 0.43663287647886184),
3: (1, 0.3847458156188478, 0.63663287647886184),
4: (1, 0.777822743459132, 0.99263085285513482),
6: (1, 0.5847458156188478, 0.93663287647886184),
7: (1, 0.7221745078773684, 0.37021499513356027)
}

def get_color(continent):
return color_map.get(continent, 'gray')

# Define data
data = {'x': gini,
'c': np.arange(len(overall)),
's': gdp}
data['y'] = score
data['s'] = np.abs(data['s']) * len(overall)
data['z'] = -0.04597 * gini + 7.316

colours = [get_color(cont) for cont in continent]

# Fit with polyfit
b, m = np.polyfit(gini, score, 1)

# Create the regression line
line = -0.04699 * gini + 7.38486

# Define G10 countries
g10_countries = ['The United States', 'Japan', 'The Netherlands', 'The United Kingdom', 'France',
'Italy', 'Canada', 'Sweden', 'Germany', 'Belgium', 'Switzerland']

# Plot Data
plt.scatter(x='x', y='y', c=colours, s='s', edgecolors='black', linewidths=0.2, data=data)
for i, txt in enumerate(country):
if txt in g10_countries:
plt.text(gini[i], score[i], txt, fontsize=8, fontstyle='italic', ha='left', va='bottom')
plt.plot(gini, line, '-', c=(1, 0.3847458156188478, 0.63663287647886184))
plt.xlabel('Gini Index', fontweight='bold')
plt.ylabel('World Happiness Score', fontweight='bold')
plt.suptitle(r'Examining the Link Between National Inequality and Happiness', fontsize=14, fontweight='bold', y=0.93)
plt.title(r'World Happiness Score vs. the Gini Index', fontsize=12, fontstyle='italic')

# Create custom legend
handles = [plt.Line2D([], [], marker='o', color=color_map[cont], linestyle='None') for cont in color_map]
labels = ['Asia', 'Africa', 'North America', 'South America', 'Europe', 'Oceania']

plt.legend(handles, labels, loc='best')

plt.show()
