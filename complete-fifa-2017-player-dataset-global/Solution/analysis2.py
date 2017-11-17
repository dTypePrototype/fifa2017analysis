# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 23:15:51 2017

@author: admin
"""
#importing the required packages
import numpy as np
import pandas as pd
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

#Importing the data
path = "C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/"
data = pd.read_csv(path+'FullData.csv')

#selection of the particular columns
cols2=['Ball_Control','Dribbling','Marking','Sliding_Tackle','Standing_Tackle','Aggression','Reactions',
'Interceptions','Vision','Composure','Crossing','Acceleration','Speed','Stamina','Strength','Balance',
'Agility','Jumping','Heading','Shot_Power','Finishing','Long_Shots','Freekick_Accuracy']

#creating the dataframe of selecting columns
field_behv = data[cols2]

#calculating the mean of all the attributes
mean = field_behv.mean()

#printing the Mean
print('Mean of all Attributes:')
print(mean)

#ploting the mean
Y = [57.97276552194678,54.80287696156471,44.23032749602002,45.56549920400273,
47.44109620195588,55.92017284512168,61.77058221514669,46.79406413463725,
52.707869001591995,55.85313850352513,49.74107345917671,65.28786672731408,
65.48385262679099,63.47691607914487,65.08585399135774,64.00881282692745,
63.20673186263361,64.91852399363202,52.39310893791221,55.581191721628386,
45.15760745963156,47.40317261769388,43.38344325676598]

X = ['Ball_Control','Dribbling','Marking','Sliding_Tackle','Standing_Tackle','Aggression','Reactions',
      'Interceptions','Vision','Composure','Crossing','Acceleration','Speed','Stamina','Strength','Balance',
      'Agility','Jumping','Heading','Shot_Power','Finishing','Long_Shots','Freekick_Accuracy'] 

total = [0.3,1.3,2.3,3.3,4.3,5.3,6.3,7.3,8.3,9.3,10.3,11.3,12.3,13.3,14.3,15.3,16.3,17.3,18.3,19.3,20.3,21.3,22.3]


f1=plt.figure(1)
p1 = plt.bar(range(23), Y, 0.5)
plt.xlabel("Attributes")
plt.ylabel("Mean")
autolabel(p1)
p1[11].set_color('red')
p1[12].set_color('red')
p1[14].set_color('red')
p1[15].set_color('green')
p1[16].set_color('yellow')
p1[13].set_color('yellow')
p1[17].set_color('green')
plt.xticks(total, X, rotation=90)
plt.yticks(np.arange(0, 80, 10))
plt.title('Field Behaviour by mean')
f1.show()


#calculating the median of all the attributes
median = field_behv.median()

#printing the SD
print('Median of all Attributes:')
print(median)

#ploting the Median
Y=[63,60,48,51,54,59,62,52,54,57,54,68,68,66,66,65,65,65,56,59,48,52,42]
f2=plt.figure(2)
p1 = plt.bar(range(23), Y, 0.5)
plt.xlabel("Attributes")
plt.ylabel("Median")
autolabel(p1)
p1[11].set_color('red')
p1[12].set_color('red')
p1[13].set_color('green')
p1[14].set_color('green')
p1[15].set_color('yellow')
p1[16].set_color('yellow')
p1[17].set_color('yellow')
plt.xticks(total, X, rotation=90)
plt.yticks(np.arange(0, 90, 10))
plt.title('Field Behaviour by median')
f2.show()

#calculating the mode of all the attriubutes
mode = field_behv.mode()

#printing the mode
print('Mode of all Attributes:')
print(mode)

#ploting the mode
Y = [65,65,	64,64,66,70,65,64,59,65,62,68,68,70,70,65,72,70,58,68,60,59,42]
f3=plt.figure(3)
p1 = plt.bar(range(23), Y, 0.5)
plt.xlabel("Attributes")
plt.ylabel("Mode")
autolabel(p1)
p1[11].set_color('yellow')
p1[12].set_color('yellow')
p1[13].set_color('green')
p1[14].set_color('green')
p1[5].set_color('green')
p1[16].set_color('red')
p1[17].set_color('green')
plt.xticks(total, X, rotation=90)
plt.yticks(np.arange(0, 90, 10))
plt.title('Field Behaviour by mode')
f3.show()
f3.savefig("Mode.png")


#calculating the standard deviation
sd = field_behv.std()

#printing the SD
print('Standard Deviation of all Attributes:')
print(sd)

#ploting the SD
Y = [16.83477914160184,18.913856927552175,21.5617028636695,21.51517868378594,
21.82781517739478,17.445464371518455,9.27521037220049,20.494714581296034,
14.589446111756574,13.48599440442466,18.457977316700177,14.436295831413839,
14.100614851107697,15.477376758689498,12.532989073544744,13.720287806498058,
14.61816332441314,11.430806830380563,17.47370319474041,17.60015497274415,
19.374428000510186,19.211887239466577,17.701902992977008]
f4=plt.figure(4)
p1 = plt.bar(range(23), Y, 0.5)
plt.xlabel("Attributes")
plt.ylabel("standrad deviation")
autolabel(p1)
p1[2].set_color('red')
p1[3].set_color('red')
p1[4].set_color('red')
p1[7].set_color('green')
p1[20].set_color('yellow')
p1[21].set_color('yellow')
plt.xticks(total, X, rotation=90)
plt.yticks(np.arange(0, 25, 5))
plt.title('Field Behaviour by standard deviation')
f4.show()