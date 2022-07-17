# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:55:28 2022

@author: jkd
"""
import copy


#Compares goal and initial state
def compare(s,g):                              
    if s==g:
        return 1
    else:
        return 0
       
#Adds elements to the queue
def enqueue(new_state):                      
    global queue
   
    if new_state[1] not in visited:
        queue=queue+[new_state]
    else:
        return queue

#Removes and returns shortest element from the queue
def dequeue():                               
    global queue
    for i in range(len(queue)):
        elem=queue[i]
        if elem[0]<=dist1:
            new_state=queue[i]
            queue=[]
            return new_state

#Calculates distance/Number of operations to perform
def distance(s3,g):                          
    c=0
    for i in range(len(s3)):
        for j in range(len(s3[0])):
            if s3[i][j]!=g[i][j]:
             c=c+1
    return c
           
queue=[]
visited=[]
  
#Finds position of the blank block     
def find_pos(s1):                            
    for i in range(len(s1)):
        for j in range(len(s1[0])):
            if s1[i][j]==0:
                l=[]
                l+=[i,j]
                return l
    return 0
#check and move the blank block up   
def up(s,pos):                              
    row=pos[0]
    col=pos[1]
    s1=copy.deepcopy(s)
    if row==0:
        return s
    else:
      s1[row][col]=s1[row-1][col]
      s1[row-1][col]=0
      return s1
  
#check and move the blank block left     
def left(s,pos):
    row=pos[0]
    col=pos[1]
    s2=copy.deepcopy(s)
    if col==0:
        return s
    else:
      s2[row][col]=s2[row][col-1]
      s2[row][col-1]=0
      return s2
 
#check and move the blank block right
def right(s,pos):
    s3=copy.deepcopy(s)
    row=pos[0]
    col=pos[1]
    if col==2:
        return s
    else:
      s3[row][col]=s3[row][col+1]
      s3[row][col+1]=0
      return s3

#check and move the blank block down
def down(s,pos):
    row=pos[0]
    col=pos[1]
    s4=copy.deepcopy(s)
    if row==2:
        return s
    else:
      s4[row][col]=s4[row+1][col]
      s4[row+1][col]=0
      return s4

def main():
    global visited
    global dist1
    s0=[[2,0,3],[1,8,4],[7,6,5]]
    g=[[1,2,3],[8,0,4],[7,6,5]]
    while(1):
        dist=distance(s0,g)
        dist1=dist
        print("Distance : ",dist)
        pos=find_pos(s0)        #find position of blank block
        
        new_state=up(s0,pos)
        d1=distance(new_state,g)
        i=compare(g,new_state)  #check if the current state is the required state
        if(i==1):
            print("found")
            exit(0)
        else:
            t1=[]
            t1=t1+[new_state,d1]
            enqueue([d1,new_state])

        new_state=down(s0,pos)
        d2=distance(new_state,g)
        i=compare(g,new_state)  #check if the current state is the required state
        if(i==1):
            print("found")
            exit(0)
        else:
            t2=[]
            t2=t2+[new_state,d2]
            enqueue([d2,new_state])
   
        new_state=left(s0,pos)
        d3=distance(new_state,g)
        i=compare(g,new_state)  #check if the current state is the required state
        if(i==1):
            print("found")
            exit(0)
        else:
            t3=[]
            t3=t3+[new_state,d3]
            enqueue([d3,new_state])   
     
        new_state=right(s0,pos)
        d4=distance(new_state,g)
        i=compare(g,new_state)  #check if the current state is the required state
        if(i==1):
            print("found")
            exit(0)
        else:
            t3=[]
            t3=t3+[new_state,d3]
            enqueue([d4,new_state])
   
        state=dequeue()
        state1=state[1]
        if (dist>=state[0]):
            print("State reached is:")
            print(state)
            return
        else:
          s0=state1

if __name__=="__main__":
    main()
