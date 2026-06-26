'''
3 write a function to calculate factorial and return it(non negative number ).
'''

def fact(n):
    result=1
    if n>0:
        for i in range(1,n+1):
            result = result * i

    elif n==1 or n==0 :
        result=1

    else:
        return "invalid"

    return result

print(fact(4))
print(fact(0))
print(fact(1))
print(fact(-2))
print(fact(7))
