# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 20:56:53 2017

@author: Abhishek
"""
# Importing Library


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ggplot

path = "C:/Users/Abhishek Sharma/Desktop/5th sem project/complete-fifa-2017-player-dataset-global/"
FullData=pd.read_csv(path+'FullData.csv')
stamina_desc100 <- head(arrange(FullData, desc(Stamina)), n=100)
#stamina_list <- stamina_desc100 %>% group_by(Nationality)  %>% summarise(n = n()) %>% arrange(descending())

#datatable(stamina_list, style="bootstrap", class="table-condensed", options = list(dom = 'tp',scrollX = TRUE))