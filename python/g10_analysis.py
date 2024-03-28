import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

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
def random_colour():
r = 1
g = random.uniform(0, 1)
b = random.uniform(0, 1)
return (r, g, b)

colours = [random_colour() for _ in range(len(overall))]

# Rename Countries
dataframe['Country or region'] = dataframe['Country or region'].replace(
{'The United States': 'The US'}
)
dataframe['Country or region'] = dataframe['Country or region'].replace(
{'The United Kingdom': 'The UK'}
)

# Define G10 countries
g10_countries = ['The US', 'Japan', 'The Netherlands', 'The UK', 'France',
'Italy', 'Canada', 'Sweden', 'Germany', 'Belgium', 'Switzerland']
g10_data = dataframe[dataframe['Country or region'].isin(g10_countries)]

# Calculate averages
g10_average = np.mean(g10_data['Score'])
global_average = np.mean(score)

# Plot Data
plt.bar(x=g10_data['Country or region'], height=g10_data['Score'], color=colours)
plt.xlabel('G10 Countries', fontweight='bold')
plt.ylabel('World Happiness Score', fontweight='bold')
plt.suptitle(r'Examining Happiness in the G10 Countries', fontsize=14, fontweight='bold', y=0.94)
plt.title(r'Happiness Score in G10 vs. Average World Happiness Score Globally', fontsize=12, fontstyle='italic')

# Add average lines
plt.axhline(y=g10_average, color=(1, 0.6221745078773684, 0.47021499513356027), linestyle='--', label='G10 Average')
plt.axhline(y=global_average, color=(1, 0.3847458156188478, 0.63663287647886184), linestyle='--', label='Global Average')

# Add "*" for siginificance
plt.text(len(g10_countries)-1, g10_average, "*", color=(1, 0.6221745078773684, 0.47021499513356027), fontweight='bold', fontsize=12, ha='right', va='bottom')

# Create custom legend
plt.legend()

plt.show()