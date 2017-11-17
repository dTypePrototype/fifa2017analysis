# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 22:18:14 2017

@author: admin
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1*height,
                '%d' % int(height),
                ha='center', va='bottom')


path = "C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/"
data = pd.read_csv(path+'FullData.csv')

cols = ['Name','Age','Nationality','Ball_Control','Club',
       'Acceleration', 'Speed', 'Stamina', 'Strength', 'Balance',
       'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing',
       'Long_Shots', 'Curve', 'Freekick_Accuracy', 'Penalties', 'Volleys']
player_data = data[cols]

print('Best Three Goal Scorers')

#finding the Rank 1 goal scorer
player = player_data.loc[player_data['Finishing'] == 95 ]
name=player['Name'].item()
print('1',name)
f1=plt.figure(1)
plt.title(name)
img = plt.imread(path+'Pictures/'+name+'.png')
plt.imshow(img)
f1.savefig('Rank 1.png')
Y=[player['Acceleration'].item(),player['Speed'].item(),player['Stamina'].item() ,
       player['Strength'].item() ,player['Balance'].item() ,player['Agility'].item(),
        player['Jumping'].item(),player['Heading'].item() ,player['Shot_Power'].item() ,
        player['Finishing'].item() ,player['Long_Shots'].item(),player['Curve'].item() ,
        player['Freekick_Accuracy'].item() ,player['Penalties'].item() ,
        player[ 'Volleys'].item(),player[ 'Ball_Control'].item()]

X= ['Acceleration', 'Speed', 'Stamina', 'Strength', 'Balance',
       'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing',
       'Long_Shots', 'Curve', 'Freekick Accuracy', 'Penalties', 'Volleys','Ball_Control']
       
title = player['Name'].item(),player['Nationality'].item(),player['Age'].item(),player['Club'].item()
total1=[0.3, 1.3,2.3,3.3,4.3,5.3,6.3,7.3,8.3,9.3,10.3,11.3,12.3,13.3,14.3,15.3]
total= np.arange(16)
import matplotlib.pyplot as plot
f2=plt.figure(2)
p1 = plot.bar(total, Y, 0.5)
p1[9].set_color('r')
plt.xticks(total1, X, rotation=90)
plt.yticks(np.arange(0, 110, 10))
plt.xlabel("Attributes")
plt.ylabel("Values")
plt.title(title)
autolabel(p1)
f2.show()

#finding the Rank 2 goal scorer
player = player_data.loc[player_data['Finishing'] == 94 ]
name=player['Name'].item()
print('2',name)
f3=plt.figure(3)
img = plt.imread(path+'Pictures/'+name+'.jpg')
plt.title(name)
plt.imshow(img)
f3.savefig('Rank 2.png')
Y=[player['Acceleration'].item(),player['Speed'].item(),player['Stamina'].item() ,
       player['Strength'].item() ,player['Balance'].item() ,player['Agility'].item(),
        player['Jumping'].item(),player['Heading'].item() ,player['Shot_Power'].item() ,
        player['Finishing'].item() ,player['Long_Shots'].item(),player['Curve'].item() ,
        player['Freekick_Accuracy'].item() ,player['Penalties'].item() ,
        player[ 'Volleys'].item(),player[ 'Ball_Control'].item()]

X= ['Acceleration', 'Speed', 'Stamina', 'Strength', 'Balance',
       'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing',
       'Long_Shots', 'Curve', 'Freekick Accuracy', 'Penalties', 'Volleys','Ball_Control']
       
title = player['Name'].item(),player['Nationality'].item(),player['Age'].item(),player['Club'].item()
f4=plt.figure(4)
p1 = plot.bar(total, Y, 0.5)
p1[9].set_color('r')
plt.xticks(total1, X, rotation=90)
plt.yticks(np.arange(0, 110, 10))
plt.xlabel("Attributes")
plt.ylabel("Values")
plt.title(title)
autolabel(p1)
f4.show()
#finding the Rank 3 goal scorer
player = player_data.loc[player_data['Finishing'] == 93 ]
name=player['Name'].item()
print('3',name)
f5=plt.figure(5)
img = plt.imread(path+'Pictures/'+name+'.png')
plt.title(name)
plt.imshow(img)
f5.savefig('Rank 3.png')
Y=[player['Acceleration'].item(),player['Speed'].item(),player['Stamina'].item() ,
       player['Strength'].item() ,player['Balance'].item() ,player['Agility'].item(),
        player['Jumping'].item(),player['Heading'].item() ,player['Shot_Power'].item() ,
        player['Finishing'].item() ,player['Long_Shots'].item(),player['Curve'].item() ,
        player['Freekick_Accuracy'].item() ,player['Penalties'].item() ,
        player[ 'Volleys'].item(),player[ 'Ball_Control'].item()]

X= ['Acceleration', 'Speed', 'Stamina', 'Strength', 'Balance',
       'Agility', 'Jumping', 'Heading', 'Shot_Power', 'Finishing',
       'Long_Shots', 'Curve', 'Freekick Accuracy', 'Penalties', 'Volleys','Ball_Control']
       
title = player['Name'].item(),player['Nationality'].item(),player['Age'].item(),player['Club'].item()

f6=plt.figure(6)
p1 = plot.bar(total, Y, 0.5)
p1[9].set_color('r')
plt.xticks(total1, X, rotation=90)
plt.yticks(np.arange(0, 110, 10))
plt.xlabel("Attributes")
plt.ylabel("Values")
plt.title(title)
autolabel(p1)
f6.show()

