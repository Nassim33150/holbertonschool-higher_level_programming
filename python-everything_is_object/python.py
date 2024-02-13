def modify_mutable(lst):
    lst.append(4)  # Modification of list inside a fonction
    print("Inside function:", lst)

my_list = [1, 2, 3]
modify_mutable(my_list)
print("Outside function:", my_list)  # The list has been modified
