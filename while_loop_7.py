print('Enter the String to be printed in reverse chrs....')
s=input()
l=len(s)
count=l-1
while(count>=0):
    print(s[count:count+1])
    count=count-1