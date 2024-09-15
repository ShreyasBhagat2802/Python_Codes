#Program for Find remainder of list multiplication divided by n
def List_Reminder(num_list):
    new_list = []
    reminder = 0
    if not num_list:
        print("Tuple is empty")
    else:
        multi = 1
        for i in num_list:
            multi *= i
        print("Multiplication is ",multi)
        if multi < n:
            print("The value of divisior is large")
        else:
            remainder = multi % n
        print("The reminder is ",remainder)
        new_list.append(multi)
        new_list.append(remainder)

    mul_rem_tupel = tuple(new_list)
    print(mul_rem_tupel)


number_list = []
size = int(input("Enter how many number want to add "))
for i in range(0, size):
    data = int(input(f"Enter {i + 1} element "))
    number_list.append(data)

n = int(input("Enter the value of divisior "))
List_Reminder(number_list)
