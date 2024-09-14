#Program to find second largest element
number_list = []
number_count = int(input("Enter number of item in the list "))

for i in range(1, (number_count+1)):
    number = int(input('Enter the number '))
    number_list.append(number)
print(number_list)

largest = 0
second_largest = 0

for i in number_list:
    if len(number_list) == 1:
        print("Only one number")

    elif len(number_list) > 1:
        if largest == i:
            pass
        elif largest < i:
            second_largest = largest
            largest = i
        elif largest > i:
            pass
print(second_largest)

    
