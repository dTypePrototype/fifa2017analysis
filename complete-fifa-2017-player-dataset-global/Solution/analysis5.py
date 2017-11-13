# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 21:56:11 2017

@author: Abhishek
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading the complete data
path = "C:/Users/Abhishek Sharma/Desktop/5th sem project/complete-fifa-2017-player-dataset-global/"
data = pd.read_csv(path+'FullData.csv')

cols = ['Name','Contract','Club_Joining','period','Contract_Expiry','Club', 'Rating', 'Age','Nationality']
player_data = data[cols]

contract= player_data.iloc[:,1]
contract.dropna(how='any',axis=0,inplace = True)


#Player having the longest contract period
period = player_data.iloc[:,3]
period.dropna(how='any',axis=0,inplace = True)

#calculating the average contract period of the players. 
print()
avg=period.mean()
print('Average contract period of each player',avg,'years')

#finding the max period of the player
print()
m=max(period)
print("Longest contract period : ",m)

#printing the index of the player having the max contract period. 
print()
print("Index of longest contract period :",period.argmax())

#finding and printing the details of the player having the max contract period.
print()
cont_player = player_data.loc[player_data['period'] == m]
cont_plr_name = cont_player['Name'].item()
cont_plr_age = cont_player['Age'].item()
cont_plr_cdate = cont_player['Contract_Expiry'].item()
cont_plr_jdate = cont_player['Club_Joining'].item()
cont_plr_club = cont_player['Club'].item()
cont_plr_nation = cont_player['Nationality'].item()
cont_plr_rating = cont_player['Rating'].item()
print("Details of player having MAX contarct period")
print("Player name : ",cont_plr_name)
print("Player age : ",cont_plr_age)
print("Player contract Expiry : ",cont_plr_cdate)
print("Player club joining date : ",cont_plr_jdate)
print("Player club : ",cont_plr_club)
print("Player rating : ",cont_plr_rating)
print("Player nationality : ",cont_plr_nation)

#Players having the smallest contract period
print()
period_low= player_data.iloc[:,3]
ma=min(period_low)
print('Smallest contract period',ma)
print("Index of smallest contract period :",period_low.argmin())

#"Total 341+1 players are there who has club joining and contract expiry date in the same year."
print()
print("Total 341 players are there who has club joining and contract expiry date in the same year")
cont_player_low_total_0 = player_data.loc[player_data['period'] == ma]

#finding and printing the details of the player having the min contract period.
print()
cont_player_low=player_data.iloc[13236,:]
cont_plr_name_low = cont_player_low['Name']
cont_plr_age_low = cont_player_low['Age']
cont_plr_cdate_low = cont_player_low['Contract_Expiry']
cont_plr_jdate_low = cont_player_low['Club_Joining']
cont_plr_club_low = cont_player_low['Club']
cont_plr_nation_low = cont_player_low['Nationality']
cont_plr_rating_low = cont_player_low['Rating'].item()
print("Details of player having MIN contarct period")
print("Player name : ",cont_plr_name_low)
print("Player age : ",cont_plr_age_low)
print("Player contract Expiry : ",cont_plr_cdate_low)
print("Player club joining date : ",cont_plr_jdate_low)
print("Player club : ",cont_plr_club_low)
print("Player rating : ",cont_plr_rating_low)
print("Player nationality : ",cont_plr_nation_low)

#ploting the histogram
f1 = plt.figure(1)
p1=plt.hist(contract,bins=range(1,9),rwidth=0.5)
plt.xlabel('contract')
plt.ylabel('No. of players')
plt.xticks([1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5],[2017,2018,2019,2020,2021,2022,2023] , rotation=90)
plt.yticks(np.arange(0, 5500, 500))
plt.title('Contract Expiry')
f1.show()
f1.savefig('bar.png')

#ploting the piechart.
explode=[0.1,0,0,0,0,0.1,0]
labels=[2017,2018,2019,2020,2021,2022,2023]
per=[25.75,23.16,16.17,19.83,5.54,4.45,5.08]
f2 = plt.figure(2)
p1 = plt.pie(per,explode=explode,labels=labels,startangle=90)
plt.title('Contract Expiry')
f2.show()
f2.savefig('pie.png')
