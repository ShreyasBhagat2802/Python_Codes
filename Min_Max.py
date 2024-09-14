#Program to print Maximum and Minimum K elements in Tuple
number_tuple = (3,55,37,4,5,6,9,67,34,98)

k_value = int(input("enter the how many maximum and minimum number to print"))

min_max = []

number_list = list(number_tuple)
number_list.sort()
print(number_list)
for i in number_tuple:
    if len(number_tuple) == 1:
        print("Only one number is there")
    elif len(number_tuple) > 1:
        min_max[0:(k_value)]=number_list[0:(k_value)]
        min_max[k_value:len(number_list)] = number_list[(len(number_list)-k_value):(len(number_list))]
number_tuple = tuple(min_max)
print(number_tuple)
