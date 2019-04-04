import csv
import numpy as np
import pandas as pd
import scipy.io

table_3=pd.read_csv("table_3.csv")
keys = table_3.iloc[:,0]+"_" +table_3.iloc[:,1]+"_"+"Transition"

quintile1condition = table_3.iloc[:,18:23]
quintile2condition = table_3.iloc[:,23:28]
quintile3condition = table_3.iloc[:,28:33]
quintile4condition = table_3.iloc[:,33:38]
quintile5condition = table_3.iloc[:,38:43]

variables = {}
for i in range(0,len(keys)):
	transition = np.zeros((5,5))
	transition[0]=quintile1condition.iloc[i]
	transition[1]=quintile2condition.iloc[i]
	transition[2]=quintile3condition.iloc[i]
	transition[3]=quintile4condition.iloc[i]
	transition[4]=quintile5condition.iloc[i]
	variables[keys[i]]=transition


table_1 = pd.read_csv("table_1.csv")
density_columns = table_1.iloc[:,7:12]
for i in range(0,5):
	population_distribution = np.zeros((5,1))
	population_distribution[0]=sum(density_columns.iloc[0:20,i])
	population_distribution[1]=sum(density_columns.iloc[20:40,i])
	population_distribution[2]=sum(density_columns.iloc[40:60,i])
	population_distribution[3]=sum(density_columns.iloc[60:80,i])
	population_distribution[4]=sum(density_columns.iloc[80:100,i])
	name = list(density_columns)[i]
	name1 = name.replace("density_","").replace("_pooled","")+"_population_distribution"
	variables[name1]=population_distribution

#scipy.io.savemat("transistion_and_distributions.mat",variables)	
