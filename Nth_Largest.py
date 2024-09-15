number_list = [5]
number_list = []
number_count = int(input("Enter number of item in the list "))

for i in range(1, (number_count+1)):
    number = int(input('Enter the number '))
    number_list.append(number)
print(number_list)

Nth_number = int(input("Enter the Nth last number wnat to find "))

new_list = []
copy = 0

if Nth_number > len(number_list):
    print("Cannot find Nth large number as length of list less")
else:
    for i in range(1, Nth_number+1):
        large = 0
        for j in number_list:
            if j not in new_list:
                if j > large:
                    large = j
                else:
                    pass
            else:
                pass
        copy = large
        new_list.append(large)      
print("Nth largest element in the list is ",new_list[-1])