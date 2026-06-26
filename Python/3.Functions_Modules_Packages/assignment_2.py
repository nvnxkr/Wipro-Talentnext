'''
2 write a function to return reverse of a string.
sample : "abcd1234"
output : "4321dcba"

'''

def revs(s):
    rev_s=""
    for char in s:
        rev_s= char +rev_s
    return rev_s

s1="harshbabu01"
print(revs(s1))
    