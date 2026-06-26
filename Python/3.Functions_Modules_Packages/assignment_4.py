'''
# 4 write a function to take string and print number of upper case and lower case in it .

'''
def count(str):
    ucount=0
    lcount=0
    for char in str:
        if char.isupper():
            ucount+=1
        elif char.islower():
            lcount+=1
    return ucount,lcount
s="thisISMEandYou"
print(count(s))