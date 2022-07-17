# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:55:28 2022

@author: jkd
"""
import copy
q=[]
visited=[]

#count the number of misplaced blocks
def heuristic(s0,g):
    count=0
    for i in range(len(s0)):
        for j in range(len(s0[0])):
            if s0[i][j]!=g[i][j]:
                count=count+1
    return count
#adding element to the q list
def enqueue(new_state):
    global q
    global visited
    if new_state[1] not in visited:
        q=q + [new_state]
#removing element from q which has least heuristic value
def dequeue():
    global q
    q.sort()
    new_state=q[0]
    #q0=[] 
    for i in range(1,len(q)-1):
        del(q[i])
    print('the value of beamed queue is ')
    print(q)
    del q[0]    
    return new_state

#checking if the current state is our final state
def compare(s0,g):
    if s0==g:
        return 1
    else:
        return 0
# find the position of blank space/zero and return it
def findpos(s0):
    for i in range(len(s0)):
        for j in range(len(s0[0])):
            if s0[i][j]==0:
                l=[]
                l=l+[i,j]
                return l
      
#check and move the blank block up
def up(s0):
    l=findpos(s0)
    row=l[0]
    col=l[1]
    s1=copy.deepcopy(s0)
    if row==0:
        return s0
    else:
        s1[row][col]=s1[row-1][col]
        s1[row-1][col]=0
        return s1
#check and move the blank block left
def left(s0):
    l=findpos(s0)
    row=l[0]
    col=l[1]
    s1=copy.deepcopy(s0)
    if col==0:
        return s0
    else:
        s1[row][col]=s1[row][col-1]
        s1[row][col-1]=0
        return s1
#check and move the blank block down
def down(s0):
    l=findpos(s0)
    row=l[0]
    col=l[1]
    s1=copy.deepcopy(s0)
    if row==2:
        return s0
    else:
        s1[row][col]=s1[row+1][col]
        s1[row+1][col]=0
        return s1
#check and move the blank block right
def right(s0):
    l=findpos(s0)
    row=l[0]
    col=l[1]
    s1=copy.deepcopy(s0)
    if col==2:
        return s0
    else:
        s1[row][col]=s1[row][col+1]
        s1[row][col+1]=0
        return s1

def main():
    global visited
    global beta
    beta=2
    s0=[[2,8,3],[1,0,4],[7,6,5]]
    g=[[1,2,3],[8,0,4],[7,6,5]]
    if compare(s0,g):
            print("Goal state reached")
            return
    count=0
    while(1):               #loop goes off until the goal state is reached
        count=count+1
        new_state=up(s0)
        if compare(new_state,g):
            print("Goal state reached")
            print(count)
            return
        h=heuristic(new_state,g)
        h1=[]
        h1=h1+[h,new_state]
        enqueue(h1)         #adding the heuristic formed by the up command

        new_state=down(s0)
        if compare(new_state,g):
            print("Goal state reached")
            print(count)
            return
        h=heuristic(new_state,g)
        h1=[]
        h1=h1+[h,new_state]
        enqueue(h1)         #adding the heuristic formed by the down command

        new_state=left(s0)
        if compare(new_state,g):
            print("Goal state reached")
            print(count)
            return
        h=heuristic(new_state,g)
        h1=[]
        h1=h1+[h,new_state]
        enqueue(h1)         #adding the heuristic formed by the left command

        new_state=right(s0)
        if compare(new_state,g):
            print("Goal state reached")
            print(count)
            return
        h=heuristic(new_state,g)
        h1=[]
        h1=h1+[h,new_state]
        enqueue(h1)         #adding the heuristic formed by the right command

        state=dequeue()
        visited=visited+[s0]
        s0=state[1]         #performing the command which has least heuristic value  

if __name__=="__main__":
    main()