#program to perform simple mathematical operations on twi numbers
a=int(input('Enter the first number \nFirst number = '))
b=int(input('Enter the second number \nSecond number = '))
c=input('Enter the operators(+,-,*,/)? \n')
if c=='+':
    d=a+b
    print('The sum of',a,'&',b,'=',d)
elif c=='-':
    d=a-b
    print('The substraction of',a,'&',b,'=',d)
elif c=='*':
    d=a*b
    print('The multiplication of',a,'&',b,'=',d)
elif c=='/':
    d=a/b
    print('The division of',a,'&',b,'=',d)
exit