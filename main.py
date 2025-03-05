import numpy as np 
import matplotlib.pyplot as plt 

file1 = open('input.txt', 'r')
lines = file1.readlines()
data = [[0 for i in range(len(lines[0].split("\t")))] for i in range(len(lines))]
X, U, Y, V = [0 for i in range(len(data)*len(data[0]))], [0 for i in range(len(data)*len(data[0]))], [0 for i in range(len(data)*len(data[0]))], [0 for i in range(len(data)*len(data[0]))]

for i in range(len(lines)):
    data[i] = lines[i].split("\t")
    for j in range(len(data[i])):
        data[i][j] = float(data[i][j].replace("\n", ""))
out = open('output.txt', 'w')
counter = 0
for j in range(len(data[0])):
    for i in range(len(data)):
        
        print(counter)
        X[counter] = [j+1] 
        print(X[counter])
        Y[counter] = [len(data)-i] 
        if (j == 0):
            U[counter] = -(data[i][j+1] - data[i][j])
        elif (j == len(data[0]) - 1):
            U[counter] = -(data[i][j] - data[i][j-1])
        else:
            U[counter] = -(
                (data[i][j+1] - data[i][j]) +
                (data[i][j] - data[i][j-1])    
            ) / 2

        if (i == 0):
            V[counter] = data[i+1][j] - data[i][j]
        elif (i == len(data) - 1):
            V[counter] = data[i][j] - data[i-1][j]
        else:
            V[counter] = (
                (data[i+1][j] - data[i][j]) +
                (data[i][j] - data[i-1][j])    
            ) / 2
        print(X[counter])
        counter += 1
  
# Creating plot 
print(str(X) + "-X")
plt.quiver(X, Y, U, V, color='b', units='xy', scale=1) 
  
# x-lim and y-lim 
plt.xlim(0, 28) 
plt.ylim(0, 20) 
  
# Show plot with grid 
plt.grid() 
plt.show() 
