a=eval(input("enter 1st subject marks:"))
b=eval(input("enter 2nd subject marks:"))
c=eval(input("enter 3rd subject marks:"))
d=eval(input("enter 4th subject marks:"))
e=eval(input("enter 5th subject marks:"))
f=eval(input("enter 6th subject marks:"))
p=(a+b+c+d+e+f)/600*100
if(p>=75):
    print('A+ Grade')
if(p>=65 and p<75):
    print('A Grade')
if(p>=50 and p<65):
    print('B Grade')
if(p>=35 and p<50):
    print('C Grade')
if(p<35):
    print('D Grade')
