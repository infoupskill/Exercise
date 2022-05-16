#generate random numbers between 10 to 100 for 50
import random
i=0
stumarks=[]
while(i<50):
    marks = random.randint(10,100)
    stumarks.append(marks)
    i=i+1
print(stumarks)

#find the first/second class & fail count
i=0
fail_count=0
first_class_cnt=0
second_class_cnt=0

while(i<50):
    if(stumarks[i]>=75):
        first_class_cnt=first_class_cnt+1
    if(stumarks[i]>=35 and stumarks[i]<75):
        second_class_cnt=second_class_cnt+1
    if(stumarks[i]<35):
        fail_count=fail_count+1
    i=i+1
   
print('First Class Count=',first_class_cnt)  
print('Second Class Count=',second_class_cnt)
print('Fail Count=',fail_count)
