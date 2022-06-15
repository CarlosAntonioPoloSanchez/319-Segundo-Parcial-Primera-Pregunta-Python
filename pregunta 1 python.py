# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def fibonacci(b):
    if b<2:
        return b
    else:
        return (fibonacci(b-1)+fibonacci(b-2))
    
print ("insertar un numero")
a=int(input())
b=""
for i in range(a):
    if i==(a-1):
        b=b+str(fibonacci(i))
    else:
        b=b+str(fibonacci(i))+", "
print(b)