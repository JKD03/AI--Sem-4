import copy
import sys
q=[]
visited=[]

def compare(state,G):
    state.sort()
    G.sort()
    if state==G:
        return True

def enqueue(new_state):                      #Adds elements to the queue
    global q
   
    if new_state[1] not in visited and new_state not in q:
        q=q+[new_state]
    else:
        return q

def dequeue():
    global q
    for i in range(len(q)):
        elem=q[i]
        if elem[0]>=dist1:
            new_state=q[i]
            q=[]
            return new_state

def find_pos(curr_elem,g):
    l=[]
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j]==curr_elem:
                l=[i,j]
                return l

def heuristic(S,G):
    h=0
    for i in range(len(S)):
        for j in range(len(S[i])):
            curr_elem=S[i][j]
            if j==0:
                elem_below_curr_elem1='ground'
            else:
                elem_below_curr_elem1=S[i][j-1]

            pos=find_pos(curr_elem,G)       #use findpos from 8 puzzle
            if pos[1]==0:
                elem_below_curr_elem2='ground'
            else:
                elem_below_curr_elem2=G[pos[0]][pos[1]-1]
    
            if  elem_below_curr_elem1==elem_below_curr_elem2:
                h=h+1
            else:
                h=h-1
    return h

def Generate_Children(S,G):
    global q
    for i in range(len(S)):
        S1=copy.deepcopy(S)
        if S1[i]==[]:
            continue
        Top_elem=S1[i].pop()
        for j in range(len(S)):
            if i!=j:
                S2=copy.deepcopy(S1)
                S2[j]+=Top_elem
                S2.sort()
                #if S2 not in q and S2 not in visited:
                h1=heuristic(S2,G)
                enqueue([h1,S2])
            
                     
        

def main():
    global visited
    global dist1
    S0=[['B','C','D','A'],[],[]]
    G=[['A','B','C','D'],[],[]]
    while(1):
        #visited+=[S0]
        h1=heuristic(S0,G)
        dist1=h1
        Generate_Children(S0,G)
        new_state=dequeue()
        if compare(new_state[1],G):
            print("Goal state reached")
            exit()
        if new_state[0]<=h1:
            print("State reached is:")
            print(new_state)
            sys.exit()
        else:
            S0=new_state[1]

if __name__=="__main__":
    main()