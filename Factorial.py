#Program for calculating factorial of a number

number = int(input("Enter number for which factorial want's to calculate "))

factorial = 1
for i in range(1, (number + 1)):
    
    factorial *= i

print(f"factorial of {number} is {factorial}")