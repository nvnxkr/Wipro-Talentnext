def create_square_dict():
    square_dict = {}
    for i in range(1, 16):
        square_dict[i] = i * i
    
    print("Dictionary containing squares:")
    print(square_dict)


create_square_dict()
