#Program to print all even and odd numbers in a range from tuple
number_tuple = (3,5,7,4,8,23,45,64,24,78,89)

even_list = []
odd_list = []

for i in number_tuple:
    if (i % 2) == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(even_list)
print(odd_list)