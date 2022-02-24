#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 16:54:57 2022

@author: miadowns
"""
import matplotlib.pyplot as plt
bar_names = []
bar_heights = []
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
textfile = open("tornado_data.txt", "r")

for line in textfile:
	bar_name, bar_height = line.split()

	bar_names.append(bar_name)
	bar_heights.append(bar_height)

plt.bar(bar_names, bar_heights)
ax.set_title('Number of Tornadoes each Month in Oaklahoma in the Year 2021')
ax.set_ylabel('Number of Tornadoes')
ax.set_xlabel('Months')
print('This graph shows the number of tornadoes that touched down in Oaklahoma in the year 2021.')

print('You can see there are a lot of tornadoes in the month of October. There are also more than usual'
      ' in the months March-May. This is known as tornado season, and November is known as the second Tornado'
      ' season. Oaklahoma is known to get a lot of tornadoes because they have very unstable atmospheric'
      ' conditions so they conduct supercell thunderstorms which turn into tornadoes. It makes sense'
      ' for the tornado seasons to be around October and the spring months because they are most prevalent'
      ' when the weather is changing so the cold and warm air is mixing together.')

print ('link:https://www.weather.gov/oun/tornadodata-ok-monthlyannual')