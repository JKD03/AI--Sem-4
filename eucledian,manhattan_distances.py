# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:55:34 2022

@author: jkd
"""
global JaskarandeepSingh
global Roll_102003486

import math
import numpy as np

#Find and return the position of element to be found
def find_pos(s,elem):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j]==elem:
                return [i,j]
    return -1

#calculate eucledian distance
def eucledian(s,g):
    #creating a matrix with all elements zero and of size len(s)*len(s[0])
    res_mat = np.zeros([len(s),len(s[0])],dtype = float)

    for x1 in range(len(s)):
        for y1 in range(len(s[0])):
            elem=s[x1][y1]
            pos=find_pos(g,elem)

            x2=pos[0]
            y2=pos[1]
            res_mat[x1][y1] = math.sqrt((x2-x1)**2 + (y2-y1)**2) #formula
    summ=0

    for i in range(len(res_mat)):
        summ += sum(res_mat[i])
        return summ

#calculate mannhattan distance
def manhattan(s,g):
    #creating a matrix with all elements zero and of size len(s)*len(s[0])
    res_mat = np.zeros([len(s),len(s[0])],dtype = float)

    for x1 in range(len(s)):
        for y1 in range(len(s[0])):
            elem=s[x1][y1]
            pos=find_pos(g,elem)

            x2=pos[0]
            y2=pos[1]

            res_mat[x1][y1] = abs(x2-x1) + abs(y2-y1) #formula
    summ=0
    for i in range(len(res_mat)):
        summ += sum(res_mat[i])
    return summ

#calculate minkowoski distance
def minkowoski(s,g,p):
    #creating a matrix with all elements zero and of size len(s)*len(s[0])
    res_mat = np.zeros([len(s),len(s[0])],dtype = float)

    for x1 in range(len(s)):
        for y1 in range(len(s[0])):
            elem=s[x1][y1]
            pos=find_pos(g,elem)
            x2=pos[0]
            y2=pos[1]
            res_mat[x1][y1] = ((abs(x2-x1)**p) + (abs(y2-y1)**p))**(1./p) #formula
    summ=0
    for i in range(len(res_mat)):
        summ += sum(res_mat[i])
    return summ

#main
if __name__ == "__main__":
    p_val = 3
    s0 = [[2,0,3],[1,8,4],[7,6,5]]
    g=[[1,2,3],[8,0,4],[7,6,5]]
    euc = eucledian(s0,g)
    man = manhattan(s0,g)
    mink = minkowoski(s0,g,p_val)
   
    print(euc,man,mink)