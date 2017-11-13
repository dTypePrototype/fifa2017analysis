# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:52:36 2017

@author: Abhishek
"""
from PIL import Image
import numpy as np
import pandas as pd
import cv2
import os
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pylab as pl




path = "C:/Users/Abhishek Sharma/Desktop/5th sem project/complete-fifa-2017-player-dataset-global/"

data = pd.read_csv(path+'FullData.csv')
print(data.isnull().sum())

cols = ['Name','Contract','Club_Joining','period','Contract_Expiry','Club_Position', 'Rating', 'Age','Nationality',
       'Preffered_Position', 'Work_Rate', 'Weak_foot', 'Skill_Moves',
       'Ball_Control', 'Dribbling', 'Marking', 'Sliding_Tackle',
       'Standing_Tackle', 'Aggression', 'Reactions', 'Attacking_Position',
       'Interceptions', 'Vision', 'Composure', 'Crossing', 'Short_Pass',
       'Long_Pass', 'Acceleration', 'Speed', 'Stamina', 'Strength', 'Balance',
       'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing',
       'Long_Shots', 'Curve', 'Freekick_Accuracy', 'Penalties', 'Volleys',
       'GK_Positioning', 'GK_Diving', 'GK_Kicking', 'GK_Handling',
       'GK_Reflexes','Club','Club_Position']

player_data = data[cols]

cols2=['Name','Nationality','Club','Ball_Control',
'Dribbling','Marking','Sliding_Tackle',
'Standing_Tackle','Aggression','Reactions',
'Interceptions','Vision','Composure','Crossing',
'Acceleration','Speed','Stamina','Strength','Balance',
'Agility','Jumping','Heading','Shot_Power','Finishing',
'Long_Shots','Freekick_Accuracy']
field_behv = data[cols2]


print('Best Three Goal Scorers')
data=data.sort(['Finishing'],ascending=[False])

goal = data['Finishing']
contract= player_data.iloc[:,1]
contract.dropna(how='any',axis=0,inplace = True)
player = player_data.loc[player_data['Finishing'] == goal[1]]
name=player['Name'].item()
print('1',name)
f1=plt.figure(1)
plt.title(name)
img = plt.imread(path+'Pictures/'+name+'.png')
plt.imshow(img)
f1.savefig('abhi.png')
Y=[player['Acceleration'].item(),player['Speed'].item(),player['Stamina'].item() ,
       player['Strength'].item() ,player['Balance'].item() ,player['Agility'].item(),
        player['Jumping'].item(),player['Heading'].item() ,player['Shot_Power'].item() ,
        player['Finishing'].item() ,player['Long_Shots'].item(),player['Curve'].item() ,
        player['Freekick_Accuracy'].item() ,player['Penalties'].item() ,
        player[ 'Volleys'].item()]

X= ['Acceleration', 'Speed', 'Stamina', 'Strength', 'Balance',
       'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing',
       'Long_Shots', 'Curve', 'Freekick Accuracy', 'Penalties', 'Volleys']
       
title = player['Name'].item(),player['Nationality'].item(),player['Age'].item(),player['Club'].item()

total1=[0.3, 1.3,2.3,3.3,4.3,5.3,6.3,7.3,8.3,9.3,10.3,11.3,12.3,13.3,14.3]
total= np.arange(15)
import matplotlib.pyplot as plot
f2=plt.figure(2)
p1 = plot.bar(total, Y, 0.5)
p1[9].set_color('r')
plt.xticks(total1, X, rotation=90)
plt.yticks(np.arange(0, 110, 10))
plt.title(title)
autolabel(p1)
f2.show()


player = player_data.loc[player_data['Finishing'] == goal[3]]
name=player['Name'].item()
print('2',name)
f3=plt.figure(3)
img = plt.imread(path+'Pictures/'+name+'.jpg')
plt.title(name)
plt.imshow(img)
Y=[player['Acceleration'].item(),player['Speed'].item(),player['Stamina'].item() ,
       player['Strength'].item() ,player['Balance'].item() ,player['Agility'].item(),
        player['Jumping'].item(),player['Heading'].item() ,player['Shot_Power'].item() ,
        player['Finishing'].item() ,player['Long_Shots'].item(),player['Curve'].item() ,
        player['Freekick_Accuracy'].item() ,player['Penalties'].item() ,
        player[ 'Volleys'].item()]

X= ['Acceleration', 'Speed', 'Stamina', 'Strength', 'Balance',
       'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing',
       'Long_Shots', 'Curve', 'Freekick Accuracy', 'Penalties', 'Volleys']
       
title = player['Name'].item(),player['Nationality'].item(),player['Age'].item(),player['Club'].item()

f4=plt.figure(4)
p1 = plot.bar(total, Y, 0.5)
p1[9].set_color('r')
plt.xticks(total1, X, rotation=90)
plt.yticks(np.arange(0, 110, 10))
plt.title(title)
#autolabel(p1)
f4.show()

player = player_data.loc[player_data['Finishing'] == goal[0]]
name=player['Name'].item()
print('3',name)
f5=plt.figure(5)
img = plt.imread(path+'Pictures/'+name+'.png')
plt.title(name)
plt.imshow(img)
Y=[player['Acceleration'].item(),player['Speed'].item(),player['Stamina'].item() ,
       player['Strength'].item() ,player['Balance'].item() ,player['Agility'].item(),
        player['Jumping'].item(),player['Heading'].item() ,player['Shot_Power'].item() ,
        player['Finishing'].item() ,player['Long_Shots'].item(),player['Curve'].item() ,
        player['Freekick_Accuracy'].item() ,player['Penalties'].item() ,
        player[ 'Volleys'].item()]

X= ['Acceleration', 'Speed', 'Stamina', 'Strength', 'Balance',
       'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing',
       'Long_Shots', 'Curve', 'Freekick Accuracy', 'Penalties', 'Volleys']
       
title = player['Name'].item(),player['Nationality'].item(),player['Age'].item(),player['Club'].item()

f6=plt.figure(6)
p1 = plot.bar(total, Y, 0.5)
p1[9].set_color('r')
plt.xticks(total1, X, rotation=90)
plt.yticks(np.arange(0, 110, 10))
plt.title(title)
autolabel(p1)
f6.show()


f7 = plt.figure(7)
p1=plt.hist(contract,bins=range(1,9),rwidth=0.5)
plt.xlabel('contract')
plt.ylabel('No. of players')
plt.xticks([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5],[2017,2018,2019,2020,2021,2022,2023] , rotation=90)
plt.yticks(np.arange(0, 5500, 500))
plt.title('Contract Expiry')
f7.show()

explode=[0.1,0,0,0,0,0.1,0]
labels=[2017,2018,2019,2020,2021,2022,2023]
per=[25.75,23.16,16.17,19.83,5.54,4.45,5.08]
f8 = plt.figure(8)
p1 = plt.pie(per,explode=explode,labels=labels,startangle=90)
plt.title('Contract Expiry')
f8.show()
f8.savefig('pie.png')


