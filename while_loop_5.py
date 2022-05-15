#fib series
print('Enter the end vlue for Fib Series...')
n=int(input())
count=0
x=1
y=2
print(x)
print(y)
while(count<n):
    z=x+y
    print(z)
    x=y
    y=z
    count=count+1