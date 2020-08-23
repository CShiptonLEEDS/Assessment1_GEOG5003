# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:14:39 2020

@author: cshipton
"""

#Agent Framework---------------------------------------------------------------

import random 
import operator
import matplotlib.pyplot
import agentframework
import csv

#Make the agents
#Building Agent class that moves, eats, stores and shares with the environment
#agents are initialised with random starting point restricted by the environment
class Agent:
    def __init__ (self, environment, agents):  
        self.x = random.randint(0,len(environment[0]))    #initialising x
        self.y = random.randint(0,len(environment))       #initialising y   
        self.environment = environment  #the environment
        self.agents = agents            #agents
        self.store = 0                  #creates a new 0 store for each Agent
    
    #Move the agents
    #by randomising the movement of each agent 
    #using 'Torus' to allow agents leaving at top or right 
    #to come back through down or left respectively
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment[0]) 
        else:
            self.y = (self.y - 1) % len(self.environment[0])
        
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment)
        else:
            self.x = (self.x - 1) % len(self.environment)
            
    
    #Create an eat method    
    #eating the environment 10 at a time
    def eat(self):
        if self.environment[self.y][self.x] > 10:
           self.environment[self.y][self.x] -= 10
           self.store += 10
    
    #check the location of an Agent and total storage
    def __str__(self):
        return "This agent is located in y" + str(self.x) + " and x" 
        + str(self.y) + " and store is " + str(self.store)
        
   
    #Create a share_with_neighbours method
    #to enable sharing resources with close agents
    #first create a distance_between method to know how close agents are             
  
    def distance_between(self, agent):
        return (((self.x- agent.x)**2) +
        ((self.y - agent.y)**2))**0.5
    
    #then share resources with close neighbours
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance  <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                print("sharing " + str(dist) + " " + str(ave))



#End---------------------------------------------------------------------------