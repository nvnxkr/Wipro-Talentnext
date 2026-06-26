def check_palindrome():
    text = input("Enter a string: ")
    
    if text == text[::-1]:
        print(f"'{text}' is a Palindrome.")
    else:
        print(f"'{text}' is not a Palindrome.")

check_palindrome()
