#Question 1
'''
import math
x=int(input("Enter the value of x : "))
n=int(input("Enter the value of n : "))
sum=0
for i in range(n):
    sum=sum+(x**i)/math.factorial(n)

print("The result is : ",sum)
'''
'''
#Question 2
#####################################################

import random
def isPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

randlist=[]
for i in range(100):
    num=random.randint(100,900)
    randlist.append(num)

print('the list on random integers is',randlist)

odd=[]
print("\n\nodd integers in it are ")
for i in randlist:
    if i%2==1:
        odd.append(i)
print(odd)
even=[]
print("\n\neven integers in it are ")
for i in randlist:
    if i%2==0:
        even.append(i)
print(even)
   
prime=[]
print("\n\nall prime numbers in it are ")
for i in randlist:
    if isPrime(i):
        prime.append(i)

print(prime)
'''
'''
#Question 3
################################################

x,y=map(int,input('Enter two numbers : ').split())
prime=[]
for i in range(x,y):
    flag=1
    for j in range(2,i):
        if i%j==0:
            flag=0
    if flag==1:
        prime.append(i)

print("number of prime numbers in given range are",prime)
'''
'''
#Question 4
################################################

list1=[1,3,4,5,9,8,6]
list2=[2,4,6,8]
common=[]
a=len(list1)
b=len(list2)

for i in list1:
    for j in list2:
        if i==j:
            common.append(i)

print("common elements are ",common)
'''   
''' 
#Question 5
################################################

years=[]
x,y=map(int,input("enter 2 years : ").split())
for i in range(x,y):
    if i%4==0:
        years.append(i)
        
print("leap years in {} and {} are {}".format(x,y,years))

'''
'''
#Question 6
##################################################

bsal=int(input("Enter Basic Salary : "))

if bsal<=10000:
    hra=0.20
    da=0.80
elif bsal<=20000:
    hra=0.25
    da=0.90
elif bsal>20000:
    hra=0.30
    da=0.95
gsal=bsal*hra*da

print("Your got {}% HRA , {}% DA and {} Gross Salary ".format(hra*100,da*100,gsal))
'''
'''
#Question 7
#########################################################

def convert(str):
    list1=[]
    list1[:0]=str
    return list1

def check(password):
    str='[@_!#$%^&*()<>?/\|}{~:]'
    a,Aa,num,spc=False,False,False,False
    special_char=convert(str)
    for i in password:
        for j in special_char:
            if i==j:
                spc=True
                break
        if i.islower() and a==False:
            a=True
        if i.isupper() and Aa==False:
            Aa=True
        if i.isdigit() and num==False:
            num=True
        if a and Aa and num:
            break
    if len(password)<6:
        print("password is too small")
    elif len(password)>16:
        print("password is too big")
    elif spc==False:
        print("Password does\'t contain any special character")
    elif num==False:
        print("Password does\'t contain any numeric")
    elif a==False:
        print("Password does\'t contain any character in lower case")
    elif Aa==False:
        print("Password does\'t contain any character in upper case")
    else:
        print("Password accepted")
    
password=input("Enter Password : ")
check(password)

'''
'''
#Question 8
##############################################################


L=[10,20,30,40,50,60,70,80]

L.append(200)
L.append(300)
print(L)
L.remove(10)
L.remove(30)
print(L)
L.sort()
print("Sorted in ascending order {} ".format(L))
print("Sorted in ascending order {} ".format(sorted(L,reverse=True)))

'''
'''
#Question 9
#############################################################

D= {1:"One", 2:"Two", 3:"Three", 4: "Four", 5:"Five"}
D[6]="Six"
print(D)
D.pop(2)2
print(D)
flg=0
for i in D.keys():
    if i==6:
        print("element 6 is present")
        flg=1
if flg==0:
    print("element 6 is not present")
    
        
print('total number of elemets in Dict D are ',len(D))

sum=0
for j in D.keys():
    sum+=j
print("Sum of elements in Dict D is ",sum)
            
'''
#Question 10
##########################################################
def function(principal,rate,time):
    return principal*((1+rate)**time)

prin,rate,time=map(float,input("enter principal amount,rate of interest and time =>").split())

print("The compound interest is ",function(prin,rate,time))
