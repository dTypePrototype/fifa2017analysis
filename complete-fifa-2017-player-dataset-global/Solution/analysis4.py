# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:55:12 2017

@author: admin
"""
import numpy as np
import pandas as pd
import collections as c
import matplotlib.pyplot as plt



#function to label the bins of the bar graph
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1*height,
                '%d' % int(height),
                ha='center', va='bottom')

#reading the fulldata file
path = "C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/"
data = pd.read_csv(path+'FullData.csv')

#selected of attributes for analysis
attributes = ['Club','Skill_Moves','Ball_Control','Dribbling','Marking',
	'Sliding_Tackle','Standing_Tackle','Aggression','Reactions','Attacking_Position','Interceptions',	'Vision',
	'Composure','Crossing','Short_Pass','Long_Pass','Acceleration','Speed','Stamina','Strength','Balance',
	'Agility','Jumping','Heading','Shot_Power','Finishing','Long_Shots','Curve','Freekick_Accuracy','Penalties',
	'Volleys','GK_Positioning','GK_Diving','GK_Kicking','GK_Handling','GK_Reflexes','period']

#creating the list of the attributes
club_ana = data[attributes]

#grouping the data group wise and calculating the mean
mean = club_ana.groupby('Club').mean()


#calculating the max mean for each group
max_mean = mean.max( axis = 1 )

#geting the max mean attribute header
attribute = mean.idxmax( axis = 1 )

#calculating the frequency of each attribute 
counter = c.Counter(attribute)

#ploting the bar group
total = [0.3,1.3,2.3,3.3,4.3,5.3,6.3,7.3]
X=['Acceleration','Agility','Balance','Jumping','Reactions','Speed','Stamina','Strength']
Y=[98, 12, 72, 91, 54, 114, 28, 165]

f1=plt.figure(6)
p1 = plt.bar(range(8), Y, 0.5)
plt.xlabel("Attributes")
plt.ylabel("No. of club")
autolabel(p1)
plt.xticks(total, X, rotation=90)
plt.yticks(np.arange(0, 180, 20))
plt.title('Attribute by club')
f1.show()
f1.savefig("Graph.png")