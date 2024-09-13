def Armstrong(num_list):
    print(num_list)
    new_list = []
    for j in num_list:
        sum = 0
        digit = 0
        if j < 0:
            print(f"{j} is invalid number")
            continue

        elif j == 0 or j > 0:
            k = j
            while k != 0:
                digit = k % 10
                sum = sum + (digit*digit*digit)
                k = k // 10
        if sum == j:
            new.append(j)
    print(new)

number_list = []
number_count = int(input("Enter number of item in the list"))

for i in range(1, (number_count+1)):
    number = int(input('Enter the number '))
    number_list.append(number)
print(number_list)

Armstrong(number_list)

    
