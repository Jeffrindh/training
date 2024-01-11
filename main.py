#Check if the first and last number of a list is the same
'''
a = input("Enter the number of list")
a=int(a)
li=[]
k=0
while (k<a):
    val=input("Enter the value")
    li.append(val)
    k=k+1
print(li)
x=len(li)
if li[0] == li[x-1]:
    print("Result is True")
else:
    print("Result is false")

'''

#Display numbers divisible by 5 from a list
'''
a = int(input("Enter the number of list"))
li=[]
re=[]
k=0
while (k<a):
    val=input("Enter the value")
    li.append(val)
    k=k+1
#print(li)
x=len(li)

for ii in range(len(li)):
    if (int(li[ii])%5==0):
        re.append(li[ii])
print(re)
'''

#Palindrome
'''
a = input("Enter the number of list")
if (a == a[::-1]):
    print("palindrome")
else:
    print("Not a palindrome")
'''

#Write a Program to extract each digit from an integer in the reverse order.
'''
a = input("Enter the number of list")

t=int(a)
res=[]
while(t>0):
    rem=t%10
    res.append(rem)
    t=t//10
print(int("".join(map(str,res))))
'''

#3)	Return the count of a given substring from a string
'''import re
string=input("Enter the string")
sub=input("Enter the string to search")
matches=len(re.findall("%s" %sub,string))
print(matches)'''


#DAY 2

#Use a loop to display elements from a given list present at odd index positions
'''a = int(input("Enter the number of list"))
li=[]
re=[]
k=0
while (k<a):
    val=input("Enter the value")
    li.append(val)
    k=k+1
#print(li)
x=len(li)
o=1
while (o<x):
    re.append(li[o])
    o=o+2

print(re)'''

#Count the total number of digits in a number

'''a=int(input("Enter the number"))
t=a
count=0
while(t>0):
    rem=t%10
    t=t//10
    count=count+1

print(count)
'''

#Display numbers from a list using loop

'''a=int(input("Enter the Number"))
sum=0
for i in range(1,a+1):
    sum+=i
print(sum)'''

#Print First 10 natural numbers using while loop .

'''i=10
c=1
while (c<=i):
    print(c)
    c+=1
'''

#Display numbers from a list using loop

a = int(input("Enter the number of list"))
li=[]
re=[]
k=0
while (k<a):
    val=input("Enter the value")
    li.append(val)
    k=k+1
print(li)
x=len(li)
count=0
for i in range(0,x):
    if(int(li[i])<500):
        if(int(li[i])%5==0) and (int(li[i])<=150):
            re.append(li[i])
        else:
            #count+=1
            continue
    else:
          #count=x
        break
    # count=count+1

print(re)