#Generate and add 10 random numbers..
#add these 10 numbers in the list
#iterate this list and add all these 10 numbers
import random
a=[]
for i in range(0,10):
    a.append(random.randint(10,100))
print(a)
s=0
for i in range(0,10):
    s=s+a[i]
print('Sum of these 10 numbers==',s)