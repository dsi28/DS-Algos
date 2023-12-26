import numpy as np

# get average temp
num_days = input('how many days do you need? ')

temps_array = np.empty(int(num_days)) 
for i in range(0,int(num_days)):
    temp_temp=input(f'enter temp for day {i+1}: ')
    temps_array[i]= int(temp_temp)
print(np.average(temps_array))