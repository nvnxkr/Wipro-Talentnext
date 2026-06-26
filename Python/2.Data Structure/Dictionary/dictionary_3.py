def check_key():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    key = 'b'
    
    if key in my_dict:
        print(f"Key '{key}' already exists in dictionary.")
    else:
        print(f"Key '{key}' does not exist.")

check_key()
