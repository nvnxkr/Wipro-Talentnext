def alphabet_dict():
    alpha_dict = {chr(i + 96): i for i in range(1, 27)}
    
    print("Alphabet mapped to integers:")
    print(alpha_dict)

alphabet_dict()
