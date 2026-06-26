def insert_item():
    my_list = [10, 20, 30, 40]
    print(f"Original list: {my_list}")
    my_list.insert(1, 15)
    print(f"List after inserting 15 before the second element: {my_list}")

if __name__ == "__main__":
    insert_item()
