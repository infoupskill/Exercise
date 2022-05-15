#Find the string is palindrome or not...
print('Enter the string to be find for palindrome...')
s1=input()
s2=s1[::-1]
if(s1==s2):
    print('Entered String is palindrome...')
else:
    print('Entered String is not palindrome...')