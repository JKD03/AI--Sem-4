# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 22:06:40 2022

@author: jkd
"""

import copy
import sys
#initialising initial and final states
Q=[]
Goal=[[2,8,1],[0,4,3],[7,6,5]]
jaskarandeep=[[1,2,3],[8,0,4],[7,6,5]]
jkd=[]

#Find the position of Blank plate
def find_blank(jaskarandeep):
    for i in range(len(jaskarandeep)):
        for j in range(len(jaskarandeep)):
            if(jaskarandeep[i][j]==0):
                return [i,j]

#Find the position of element to be found
def find_Position(jaskarandeep,val):
    for i in range(len(jaskarandeep)):
        for j in range(len(jaskarandeep)):
            if(jaskarandeep[i][j]==val):
                return [i,j]

#Add element ot the Queue
def enqueue(Q,key):
    Q+=[key]
    return Q

#Delete top/Smallest element from the Queue
def dequeue(Q):
    if(len(Q)==0):
        return Q
    del Q[0]
    return Q

#Heuristic Manhattan Function
def Heuristic_Manhattan(jaskarandeep,Goal):
    Heuristic_Manhattan_value=0
    for i in range(len(Goal)):
        for j in range(len(Goal[0])):
            L=find_Position(Goal,jaskarandeep[i][j])
            Heuristic_Manhattan_value+=abs(i-L[0])+abs(j-L[1])
    return Heuristic_Manhattan_value

#comparing initial and final states 
def compare(jaskarandeep,G):
    if(jaskarandeep==G):
        return True
    return False
#moving the blank block to the left
def left(jaskarandeep):
    L=find_blank(jaskarandeep)
    row=L[0]
    col=L[1]
    final_State=copy.deepcopy(jaskarandeep)
    if(col==0):
        return final_State 
    final_State[row][col]=final_State[row][col-1]
    final_State[row][col-1]=0
    return final_State

#moving the blank block to the right
def right(jaskarandeep):
    L=find_blank(jaskarandeep)
    row=L[0]
    col=L[1]
    final_State=copy.deepcopy(jaskarandeep)
    if(col==len(jaskarandeep[0])-1):
        return final_State
    final_State[row][col]=final_State[row][col+1]
    final_State[row][col+1]=0
    return final_State

#moving the blank block to the up
def up(jaskarandeep):
    L=find_blank(jaskarandeep)
    row=L[0]
    col=L[1]
    final_State=copy.deepcopy(jaskarandeep)
    if(row==0):
        return final_State
    final_State[row][col]=final_State[row-1][col]
    final_State[row-1][col]=0
    return final_State

#moving the blank block to the down
def down(jaskarandeep):
    L=find_blank(jaskarandeep)
    row=L[0]
    col=L[1]
    final_State=copy.deepcopy(jaskarandeep)
    if(row==len(jaskarandeep)-1):
        return final_State
    final_State[row][col]=final_State[row+1][col]
    final_State[row+1][col]=0
    return final_State
if(compare(jaskarandeep,Goal))==True:
    exit()
def search(jaskarandeep,jkd):
    for i in range(len(jkd)):
        if(jaskarandeep==jkd[i]):
            return True
    return False

def sorting_Heuristic(Q,Goal):
    min=100000000
    j=-1
    for i in range(len(Q)):
        Heuristic_Manhattan_Value=Heuristic_Manhattan(Q[i],Goal)
        if(Heuristic_Manhattan_Value<min):
            min=Heuristic_Manhattan_Value
            j=i
    jaskarandeep=Q[j]
    del Q[j]
    return jaskarandeep

Q+=[jaskarandeep]
while(len(Q)!=0):
    jaskarandeep=sorting_Heuristic(Q,Goal)
    if(search(jaskarandeep,jkd)==False):
        jkd+=[jaskarandeep]
    if((compare(jaskarandeep,Goal))==True):
 
        print("Number of states visited = ",len(jkd))
        sys.exit()
    
    if(search(left(jaskarandeep),jkd)==False):
        # print(jaskarandeep)
        Q=enqueue(Q,left(jaskarandeep))
    if(search(right(jaskarandeep),jkd)==False):
        Q=enqueue(Q,right(jaskarandeep))
    if(search(up(jaskarandeep),jkd)==False):
        Q=enqueue(Q,up(jaskarandeep))
    if(search(down(jaskarandeep),jkd)==False):
        Q=enqueue(Q,down(jaskarandeep))