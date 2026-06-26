'''
Write a function to return the sum of all numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
'''

lst=[8,2,3,0,7]
def lsum(lst):
    sum=0
    for value in lst:
        sum=sum + value 
    return sum

print(lsum(lst))
lst1=[2,3,4,5,6,7,8,0]
print(lsum(lst1))