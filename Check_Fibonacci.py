#Program for How to check if a given number is Fibonacci number?
number = int(input("Enter the number "))
num1 = 0
num2 = 1

fibonacci = 0

while fibonacci < number:
    fibonacci = num1 + num2
    num1 = num2
    num2 = fibonacci
print(fibonacci)

if fibonacci == number:
    print(f"{number} is fibonacci number")
else:
    print(f"{number} is not fibonacci number")
    