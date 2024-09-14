#program to create a list of tuples from given list
# list having number and its cube in each tuple
def Item_Cube(num_list):
    tuple_list = []
    cube = 0
    if not num_list:
        print("list is empty")

    else:
        for j in num_list:
            new_list = []
            cube = j ** 3
            new_list.append(j)
            new_list.append(cube)
            new_tuple = tuple(new_list)
            tuple_list.append(new_tuple)
    print(tuple_list)
    print(len(tuple_list))
            
number_list = []
number_count = int(input("Enter number of item in the list "))

for i in range(1, (number_count+1)):
    number = int(input('Enter the number '))
    number_list.append(number)

Item_Cube(number_list)

