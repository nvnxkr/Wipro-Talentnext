'''
5 write a program to get even numbers from the list as output.

'''
def filter(lst):
    even=[]
    for i in lst:
        if i%2==0:
            even.append(i)

    return even

lst1=[23,2,44,56,77,54,59,21]
print(filter(lst1))