#vowles count.....
print('Enter the Sentences...')
s=input()
count_a=0
count_e=0
count_i=0
count_o=0
count_u=0
loop_count=0
while(loop_count<len(s)):
    chr=s[loop_count:loop_count+1]
    if(chr=='a'):
        count_a=count_a+1
    if(chr=='e'):
        count_e=count_e+1
    if(chr=='i'):
        count_i=count_i+1
    if(chr=='o'):
        count_o=count_o+1
    if(chr=='u'):
        count_u=count_u+1
        
    loop_count=loop_count+1
print('Vowles count .....')
print('a count is===>',count_a)
print('e count is===>',count_e)
print('i count is===>',count_i)
print('o count is===>',count_o)
print('u count is===>',count_u)
