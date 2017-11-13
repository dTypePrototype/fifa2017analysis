# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 20:07:12 2017

@author: Abhishek
"""
#importing the required liberaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading the complete data
path = "C:/Users/Abhishek Sharma/Desktop/5th sem project/complete-fifa-2017-player-dataset-global/"
df=pd.read_csv(path+'FullData.csv')
Names= pd.read_csv(path+'PlayerNames.csv')
df.assign(Index=np.nan)
df['Index'] = [v.split('/')[2] for v in Names['url']]
del df['Nationality']
del df['National_Position']
del df['National_Kit']

#defining weightage factors
a= 1
b= 2
c= 3
d= 4

#GoalKeeping Indices
df['gk_Shot_Stopper'] = (b*df.Reactions + b*df.Composure + a*df.Speed + a*df.Strength + c*df.Jumping + b*df.GK_Positioning + c*df.GK_Diving + d*df.GK_Reflexes + b*df.GK_Handling)/(2*a + 4*b + 2*c + 1*d)
df['gk_Sweeper'] = (b*df.Reactions + b*df.Composure + b*df.Speed + a*df.Short_Pass + a*df.Long_Pass + b*df.Jumping + b*df.GK_Positioning + b*df.GK_Diving + d*df.GK_Reflexes + b*df.GK_Handling + d*df.GK_Kicking + c*df.Vision)/(2*a + 4*b + 3*c + 2*d)

#Defending Indices
df['df_studds'] =  (c*df.Marking + c*df.Sliding_Tackle + c*df.Standing_Tackle + c*df.Aggression + a*df.Reactions + b*df.Interceptions + c*df.Strength)/(5*c + b + a)
df['df_sweeper'] = (c*df.Ball_Control + b*df.Reactions + b*df.Interceptions + d*df.Vision + b*df.Composure + b*df.Short_Pass + b*df.Long_Pass)/(5*b + c + d)
df['df_aerial_studds'] = (c*df.Marking + b*df.Sliding_Tackle + b*df.Standing_Tackle + c*df.Sliding_Tackle + c*df.Reactions + c*df.Interceptions + b*df.Balance + c*df.Jumping + b*df.Agility + d*df.Heading)/(5*c + 4*b + d)
df['df_wing_back'] = (b*df.Ball_Control + a*df.Dribbling + a*df.Marking + c*df.Sliding_Tackle + b*df.Standing_Tackle + c*df.Attacking_Position + d*df.Vision + c*df.Crossing + b*df.Short_Pass + b*df.Long_Pass + d*df.Acceleration +d*df.Speed + c*df.Stamina + a*df.Finishing)/(3*a + 4*b + 4*c + 3*d)

#Midfielding Indices
df['mf_controller'] = (a*df.Weak_foot + c*df.Ball_Control + a*df.Dribbling + a*df.Marking + a*df.Reactions + d*df.Vision + c*df.Composure + d*df.Short_Pass + d*df.Long_Pass)/(2*c + 3*d + 4*a)
df['mf_beast'] = (b*df.Agility + b*df.Balance + b*df.Jumping + c*df.Strength + c*df.Stamina + b*df.Speed + a*df.Acceleration + b*df.Short_Pass + d*df.Aggression + d*df.Reactions + d*df.Marking + c*df.Standing_Tackle + c*df.Sliding_Tackle + d*df.Interceptions)/(1*a + 5*b + 4*c + 4*d)
df['mf_playmaker'] = (b*df.Ball_Control + a*df.Dribbling + a*df.Marking + b*df.Reactions + d*df.Vision + c*df.Crossing + c*df.Short_Pass + c*df.Long_Pass + a*df.Curve + a*df.Long_Shots + c*df.Freekick_Accuracy)/(4*a + 2*b + 4*c + d)
df['mf_attacker'] = (b*df.Ball_Control + c*df.Dribbling + b*df.Vision + b*df.Crossing + b*df.Short_Pass + b*df.Long_Pass + c*df.Agility + a*df.Curve + c*df.Long_Shots + b*df.Freekick_Accuracy + d*df.Finishing)/(a + 6*b + 3*c + d)

#Attacking Indices
df['at_left_wing'] = (c*df.Weak_foot + c*df.Ball_Control + c*df.Dribbling + c*df.Speed + d*df.Acceleration + b*df.Vision + c*df.Crossing + b*df.Short_Pass + b*df.Long_Pass + b*df.Aggression + b*df.Agility + a*df.Curve + c*df.Long_Shots + b*df.Freekick_Accuracy + d*df.Finishing)/(a + 6*b + 6*c + 2*d)
df['at_right_wing'] = (c*df.Weak_foot + c*df.Ball_Control + c*df.Dribbling + c*df.Speed + d*df.Acceleration + b*df.Vision + c*df.Crossing + b*df.Short_Pass + b*df.Long_Pass + b*df.Aggression + b*df.Agility + a*df.Curve + c*df.Long_Shots + b*df.Freekick_Accuracy + d*df.Finishing)/(a + 6*b + 6*c + 2*d)
df['at_striker'] = (b*df.Weak_foot + b*df.Ball_Control + a*df.Vision + b*df.Aggression + b*df.Agility + a*df.Curve + a*df.Long_Shots + d*df.Balance + d*df.Finishing + d*df.Heading + c*df.Jumping + c*df.Dribbling)/(3*a + 4*b + 2*c + 3*d)


col=['Name', 'gk_Shot_Stopper', 'gk_Sweeper', 'df_studds', 'df_sweeper', 'df_aerial_studds', 'df_wing_back', 'mf_controller', 'mf_beast', 'mf_playmaker', 'mf_attacker', 'at_left_wing', 'at_right_wing', 'at_striker']
new_df=df[col]

"""Goal Keeper Selection"""
sns.set(style="white", context="talk")

f, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 15), sharex=False)

shotStopper=  new_df.sort_values('gk_Shot_Stopper', ascending=False)[:7]
x1 = np.array(list(shotStopper['Name']))
y1 = np.array(list(shotStopper['gk_Shot_Stopper']))
sweeperKeeper= new_df.sort_values('gk_Sweeper', ascending=False)[:7]
x2 = np.array(list(sweeperKeeper['Name']))
y2 = np.array(list(sweeperKeeper['gk_Sweeper']))

shotStopper= shotStopper.reset_index(drop=True)
sweeperKeeper= sweeperKeeper.reset_index(drop=True)

sns.barplot(x1,y1,palette="Greens_d",ax=ax1)
ax1.set_ylabel("Shot Stopping Score")

sns.barplot(x2, y2, palette="Greens_d", ax=ax2)
ax2.set_ylabel("Sweeping Score")

print("Our 3 best Goal Keepers are:")
print(sweeperKeeper.Name[0])
print(sweeperKeeper.Name[1])
print(shotStopper.Name[1])
