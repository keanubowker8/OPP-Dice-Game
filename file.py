import numpy as np 


mystr = '33333'
lst = set(list(mystr))
amount = 100

double = False
triple = False
a = '0'
for i in lst:
    if mystr.count(i)== 2:
        a = i

def count_numbers(mystr):
    global amount
    amount -= 10
    global double 
    double = False
    global triple 
    triple = False
    
    for i in lst:
        if mystr.count(i)== 2:
            double = True
            global a 
            a = i
            amount += 5
        if (mystr.count(a)!=2 and mystr.count(i)==3):
            amount +=  8
        if mystr.count(i)== 3:
            triple =True
        if double and triple:
            amount +=  7
        if mystr.count(i)== 4:
            amount +=  15
        if mystr.count(i)== 5:
            amount +=  30
        if (mystr=='12345' and mystr=='23456'):
            amount +=  20
        else:
            pass
            

count_numbers(mystr)
print(amount)