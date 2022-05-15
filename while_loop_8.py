#Example for nested loop....exit the loop after entered the exit...
while(1<2):
    s=input()
    count=0
    while(count<len(s) and s!='exit'):
        print(s[count:count+1])
        count=count+1
    if(s=='exit'):
        print('Bye... Program is exit...')
        break;