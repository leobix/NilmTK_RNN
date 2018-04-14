#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 10:20:01 2018

@author: leobix
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import random 
from mpl_toolkits.mplot3d import Axes3D
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import pandas as pd
import scipy
import seaborn as sns


def randomWalk1D(n):
    x=[0]
    for i in range(1,n):
        rand = random.randrange(-1,2,2)
        x.append(x[i-1]+rand)
    return x
    
#randomWalk1D(1000)

def randomWalk2D(n):
    x=[0]
    y=[0]
    for i in range(1,n):
        rand = random.randrange(-1,2,2)
        rand2 = random.randrange(-1,2,2)

        x.append(x[i-1]+rand)
        y.append(y[i-1]+rand2)

    plt.plot(x,y)
    plt.show()
   
#randomWalk2D(10000)

def randomWalk3D(n):
    x=[0]
    y=[0]
    z=[0]
    for i in range(1,n):
        rand = random.randrange(-1,2,2)
        rand2 = random.randrange(-1,2,2)
        rand3 = random.randrange(-1,2,2)
        x.append(x[i-1]+rand)
        y.append(y[i-1]+rand2)
        z.append(z[i-1]+rand3)
    
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    plt.show()


randomWalk3D(10000)



def randomWalk2DGaussian(n):
    x = [0]
    y = [0]

    for j in range(1,n):
        step_x = random.randint(0,1)
        if step_x == 1:
            x.append(x[j-1] + 1 + np.random.normal())
        else:
            x.append(x[j-1] - 1 + np.random.normal())
    
        step_y = random.randint(0,1)
        if step_y == 1:
            y.append(y[j-1] + 1 + np.random.normal())
        else:
            y.append(y[j-1] - 1 + np.random.normal())
        
    

    plt.plot(x,y)
    plt.show()
    
def randomWalk2DPareto(n,mu):
    x = [0]
    y = [0]

    for j in range(1,n):
        step_x = random.randint(0,1)
        if step_x == 1:
            x.append(x[j-1] + np.random.pareto(mu))
        else:
            x.append(x[j-1] - np.random.pareto(mu))
    
        step_y = random.randint(0,1)
        if step_y == 1:
            y.append(y[j-1] + np.random.pareto(mu))
        else:
            y.append(y[j-1] - np.random.pareto(mu))
        
    

    plt.plot(x,y)
    plt.show()
    
randomWalk2DPareto(10000,2)

def randomWalkConfined1D(n,size):
    x=[0]
    
    for i in range(1,n):
        rand = random.randrange(-1,2,2)
        pos = x[i-1]+rand
        if (pos>size):
           x.append(pos-2)
        elif (pos<-size):
            x.append(pos+2)
        else :
            x.append(pos)
        
    return x

def randomWalkConfined2D(n,size):
    x=randomWalkConfined1D(n,size)
    y=randomWalkConfined1D(n,size)
    plt.plot(x,y)
    plt.show()
    
#randomWalkConfined2D(10000,50)


def finalPosition(n,m):
    x=[]
    y=[]
    for i in range(n):
        lx = randomWalk1D(m)[m-1]
        ly = randomWalk1D(m)[m-1]
        x.append(lx)
        y.append(ly)
    sns.distplot(x)
    sns.jointplot(x=x, y=y, kind="kde")
    
finalPosition(10000,100)
    
    