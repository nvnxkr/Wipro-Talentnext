'''
6  write a function  which takes number as parameter and checks whether it is prime or not.
'''
def check(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
        
    if count>2:
        ans=True
    elif count<2:
        ans=False
    elif n<=1:
        ans=False
    elif n==2:
        ans=True

    else:
        ans=False
    return ans

print(check(7))
print(check(1))
print(check(2))
print(check(0))
print(check(54))
