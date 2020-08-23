# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:13:20 2020

@author: cshipton
"""

#MODEL-------------------------------------------------------------------------------------------------------------------------------

#Required Python Packages
import random
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv

#Parametise the model
num_of_agents = 10                 #controls how many agents we have
num_of_iterations = 100            #changes agent cordinates an arbitrary number of times
neighbourhood = 20                 #guides who agents share resources with
agents = []                        #create an empty list
carry_on = True                    #used in stopping the agent movement
environment = []                    #create an empty list to read file in

              
#Filling the list to form the enviroment using data from a in.txt file              
f = open('in.txt', newline='')      #read the text a line at a time
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) #convert to float

for row in dataset:				     #reading in the rows a row at a time
    rowlist = []                    
    for value in row:
        rowlist.append(value) 
    environment.append(rowlist)
    
f.close()                           #always close the worksheet 
               
#Make agents
for i in range(num_of_agents):  #create a set of agents
    agents.append(agentframework.Agent(environment, agents))
  

#Move, eat and share points with neighbours
#the agent movement is random
for j in range(num_of_iterations):    
    #random.shuffle(agents)        #shuffles each agent list at each iteration
    for item in range(num_of_agents):
        agents[item].move()
        agents[item].eat()
        agents[item].share_with_neighbours(neighbourhood)

#Plot graph of initial positions of each agent
matplotlib.pyplot.ylim(0, len(environment[0]))
matplotlib.pyplot.xlim(0, len(environment))
matplotlib.pyplot.imshow(environment)
for agent in range(num_of_agents): 
        matplotlib.pyplot.scatter(agents[agent].x,agents[agent].y)  
        matplotlib.pyplot.show()


#End----------------------------------------------------------------------------------------------------------------------------
