import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cm as cm
from pandas import DataFrame, read_csv

# Please scroll to the bottom of the code to uncomment the functions to run
# Read the data from CSV file
df0 = pd.read_csv("orgdata.csv")

#Select the columns which will be considered for data analysis
df = df0[['ParentLocation','Location','Dim1','FactValueNumeric']] 

def visualization_1_line_plot():
  
  '''
        Draws Line plot for the data fed. X axis denotes the Country and Y axis denotes the FactValueNumeric
        Number of plots generated = 1
  '''
  print(visualization_1_line_plot.__doc__)

  # Below written graph plotting code is broken into segments as the genders in columns are not sorted/grouped

  #Get Male (M) children count for each location
  x_m = df.loc[1::3,'Location']
  y_m = df.loc[1::3,'FactValueNumeric']
  #Get Female (F) children count for each location
  x_fm = df.loc[2::3,'Location']
  y_fm = df.loc[2::3,'FactValueNumeric']
  #Get Both sexes (M+F) children count for each location
  x_bs = df.loc[::3,'Location']
  y_bs = df.loc[::3,'FactValueNumeric']

  #Plot adjustments. You may adjust the figures below to comply with your display resolution for clarity
  plt.rcParams['figure.figsize'] = (90, 40)
  plt.rcParams['font.size'] = 20 
  plt.title('Ambient air pollution attributable deaths in children under 15 years in 2019',fontsize=60,fontweight="bold")
  plt.xlabel('Location', fontsize = 50)
  plt.xticks(rotation = '90')
  plt.ylabel('FactValueNumeric',fontsize = 50)

  #Plotting begins here
  plt.plot(x_m ,y_m ,'-r' ,linewidth =2, label='Male Children (M)')
  plt.plot(x_fm,y_fm,'--g',linewidth =2, label='Female Children (F)')
  plt.plot(x_bs,y_bs,'-.b',linewidth =2, label='Both Sexes(F+M)')
  plt.legend(prop={'size': 65})

def visualization_2_box_plot():

  '''
        Draws Line plot for the data fed. X axis denotes the Country and Y axis denotes the FactValueNumeric
        Number of plots generated = 18
  '''
  print(visualization_2_box_plot.__doc__)

  #Create a list of parent countries available to use in for loop
  pcountries = ['Africa','Americas','Eastern Mediterranean', 'Europe', 'South-East Asia', 'Western Pacific']

  for pcountry in pcountries:

    #Create a list of genders available to use in for loop
    genders = ['Male','Female', 'Both sexes']

    for gender in genders:

      country = df.loc[(df.ParentLocation == pcountry) & (df.Dim1 == gender) ,'Location'] # Extract the country based on parent location and gender
      forsort = df.loc[(df.ParentLocation == pcountry) & (df.Dim1 == gender) ,:] # This is created for sorting purpose
      factvalue = df.loc[(df.ParentLocation == pcountry) & (df.Dim1 == gender) ,'FactValueNumeric'] # Extract the factvalue based on parent location and gender

      #Sort the requried data
      top10 = forsort.sort_values('FactValueNumeric', ascending=False).head(10)

      #Plot adjustments. You may adjust the figures below to comply with your display resolution for clarity
      plt.rcParams['figure.figsize'] = (30, 20)
      plt.rcParams['font.size'] = 15
      plt.xticks(rotation = '90')
      plt.title('Ambient air pollution attributable deaths in '+ pcountry +' of ' + gender + ' children under 15 years in 2019',fontsize=20,fontweight="bold")
      plt.xlabel('Country',fontsize=20)
      plt.ylabel('FactValueNumeric',fontsize=20)
      plt.bar(top10['Location'], top10['FactValueNumeric'], width=0.5, color = cm.rainbow(np.linspace(0, 1, len(top10))))
      plt.figure()


def visualization_3_scatter_plot():

  '''
        Draws Line plot for the data fed. X axis denotes the Country and Y axis denotes the FactValueNumeric
        Number of plots generated = 1
  '''
  print(visualization_3_scatter_plot.__doc__)

  pcountries = ['Africa','Americas','Eastern Mediterranean', 'Europe', 'South-East Asia', 'Western Pacific']

  a_sum = df.loc[(df.ParentLocation == 'Africa') & (df.Dim1 =='Both sexes'),'FactValueNumeric'].sum()
  b_sum = df.loc[(df.ParentLocation == 'Americas') & (df.Dim1 =='Both sexes'),'FactValueNumeric'].sum()
  c_sum = df.loc[(df.ParentLocation == 'Eastern Mediterranean') & (df.Dim1 =='Both sexes'),'FactValueNumeric'].sum()
  d_sum = df.loc[(df.ParentLocation == 'Europe') & (df.Dim1 =='Both sexes'),'FactValueNumeric'].sum()
  e_sum = df.loc[(df.ParentLocation == 'South-East Asia') & (df.Dim1 =='Both sexes'),'FactValueNumeric'].sum()
  f_sum = df.loc[(df.ParentLocation == 'Western Pacific') & (df.Dim1 =='Both sexes'),'FactValueNumeric'].sum()

  consolidated_data = [a_sum,b_sum,c_sum,d_sum,e_sum,f_sum]

  #Plot adjustments. You may adjust the figures below to comply with your display resolution for clarity
  plt.rcParams['figure.figsize'] = (9, 9)
  plt.rcParams['font.size'] = 10
  plt.xticks(rotation = '90')
  plt.title('Total of ambient air pollution attributable deaths of children under 15 years in 2019',fontsize=15,fontweight="bold")
  plt.xlabel('Country',fontsize=10)
  plt.ylabel('FactValueNumeric',fontsize=10)
  plt.scatter(pcountries, consolidated_data ,c = cm.rainbow(np.linspace(0, 2, len(pcountries))))



# Main functions are listed below. Please uncomment to run any function

#visualization_1_line_plot()
#visualization_2_box_plot()
#visualization_3_scatter_plot()

