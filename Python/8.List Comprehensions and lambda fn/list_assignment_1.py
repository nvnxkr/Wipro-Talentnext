def odd_cubes_dict():
    input_list = [1, 2, 3, 4, 5, 6, 7]
    
    output_dict = {x: x**3 for x in input_list if x % 2 != 0}
    
    print(f"Input list: {input_list}")
    print(f"Output dictionary: {output_dict}")

odd_cubes_dict()
