number_list = []
number_count = int(input("Enter number of item in the list"))

for i in range(1, (number_count+1)):
    number = int(input('Enter the number '))
    number_list.append(number)
print(number_list)

x = 0
y = 0

for i in number_list:
    if len(number_list) == 1:
        print("Only one number")

    elif len(number_list) > 1:
        if x == i:
            pass
        elif x < i:
            y = x
            x = i
        elif x > i:
            pass
print(y)

    