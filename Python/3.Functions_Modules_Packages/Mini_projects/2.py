'''
Create a Python module with the following functions:

ispalindrome(name):--Given the user name as input, this function should
tell us whether the name is a palindrome or not.

count_the_vowels(name):--Given the user name as input, this function should
tell us how many vowels are present in it.

frequency_of_letters(name):--Given the user name as input, this function should
tell us how many times each letter appears in the
name.

Note: name will be completely in either lower case or upper case.

Import the module in another python script and test the functions by passing
appropriate inputs.

Sample input 1: bob

Sample output 1:

Yes it is a palindrome.

No of vowels: 1

Frequency of letters: b-2, o-1
'''

def ispalindrome(name: str) -> bool:
    return name == name[::-1]


def count_the_vowels(name: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return count


def frequency_of_letters(name: str) -> dict:
    freq_dict = {}
    for char in name:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict