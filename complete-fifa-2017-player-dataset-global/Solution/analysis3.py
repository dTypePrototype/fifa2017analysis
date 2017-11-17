# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 21:43:48 2017

@author: admin
"""

import numpy as np
import pandas as pd
from collections import Counter as ctr

#reading the fulldata file
path = "C:/Users/HP/fifa2017analysis/complete-fifa-2017-player-dataset-global/"
data = pd.read_csv(path+'FullData.csv')

#selected of attributes for analysis
attributes = ['Nationality','Skill_Moves','Ball_Control','Dribbling','Marking','Sliding_Tackle','Standing_Tackle',
'Aggression','Reactions','Attacking_Position','Interceptions','Vision','Composure','Crossing',
'Short_Pass','Long_Pass','Acceleration','Speed','Stamina','Strength','Balance','Agility',
'Jumping','Heading','Shot_Power','Finishing','Long_Shots','Curve','Freekick_Accuracy','Penalties',
'Volleys','GK_Positioning','GK_Diving','GK_Kicking','GK_Handling','GK_Reflexes']

#creating the list of the attributes
contenient_ana = data[attributes]

#selected of attributes for analysis
attributes=['Skill_Moves','Ball_Control','Dribbling','Marking','Sliding_Tackle','Standing_Tackle',
'Aggression','Reactions','Attacking_Position','Interceptions','Vision','Composure','Crossing',
'Short_Pass','Long_Pass','Acceleration','Speed','Stamina','Strength','Balance','Agility',
'Jumping','Heading','Shot_Power','Finishing','Long_Shots','Curve','Freekick_Accuracy','Penalties',
'Volleys','GK_Positioning','GK_Diving','GK_Kicking','GK_Handling','GK_Reflexes']


#reading continent file
continent=pd.read_csv(path+'continent.csv')

#reading the asian continent and droping the null values.
Asia=continent['Asia']
Asia.dropna(how='any',axis=0,inplace = True)

#reading the european continent and droping the null values.
Europe=continent['Europe']
Europe.dropna(how='any',axis=0,inplace = True)

#reading the south american continent and droping the null values.
SA=continent['South America']
SA.dropna(how='any',axis=0,inplace = True)

#reading the north american continent and droping the null values.
NA=continent['North America']
NA.dropna(how='any',axis=0,inplace = True)

#reading the african continent and droping the null values.
AF=continent['Africa']
AF.dropna(how='any',axis=0,inplace = True)

#selecting the asian players form the data
asian_player = pd.DataFrame()
for row in range(6):
     asian_player = asian_player.append(contenient_ana.loc[contenient_ana['Nationality'] == Asia[row] ])

#selecting the european players form the data
Europe_player = pd.DataFrame()
for row in range(33):
     Europe_player = Europe_player.append(contenient_ana.loc[contenient_ana['Nationality'] == Europe[row] ])

#selecting the south american players form the data
SA_player = pd.DataFrame()
for row in range(13):
     SA_player = SA_player.append(contenient_ana.loc[contenient_ana['Nationality'] == SA[row] ])

#selecting the north american players form the data
NA_player = pd.DataFrame()
for row in range(11):
     NA_player = NA_player.append(contenient_ana.loc[contenient_ana['Nationality'] == NA[row] ])

#selecting the african players form the data
AF_player = pd.DataFrame()
for row in range(17):
     AF_player = AF_player.append(contenient_ana.loc[contenient_ana['Nationality'] == AF[row] ])
     
#selecting the american players form the data
A_player = contenient_ana.loc[contenient_ana['Nationality'] == 'Australia' ]

#best attribute of Europien players
Avg = {}
for a in range(35):
    Avg[a] = Europe_player[attributes[a]].mean()
v=list(Avg.values())
k=list(Avg.keys())
print('Europe players are expert in = ',attributes[k[v.index(max(v))]])

#best attribute of asian players
Avg = {}
for a in range(35):
    Avg[a] = asian_player[attributes[a]].mean()
v=list(Avg.values())
k=list(Avg.keys())
print('asian_player are expert in = ',attributes[k[v.index(max(v))]])

#best attribute of SA_player
Avg = {}
for a in range(35):
    Avg[a] = SA_player[attributes[a]].mean()
v=list(Avg.values())
k=list(Avg.keys())
print('SA_player are expert in = ',attributes[k[v.index(max(v))]])

#best attribute of NA_player
Avg = {}
for a in range(35):
    Avg[a] = NA_player[attributes[a]].mean()
v=list(Avg.values())
k=list(Avg.keys())
print('NA_player are expert in = ',attributes[k[v.index(max(v))]])

#best attribute of AF_player
Avg = {}
for a in range(35):
    Avg[a] = AF_player[attributes[a]].mean()
v=list(Avg.values())
k=list(Avg.keys())
print('AF_player are expert in = ',attributes[k[v.index(max(v))]])

#best attribute of A_player
Avg = {}
for a in range(35):
    Avg[a] = A_player[attributes[a]].mean()
v=list(Avg.values())
k=list(Avg.keys())
print('A_player are expert in = ',attributes[k[v.index(max(v))]])

