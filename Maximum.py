#Maximum of three numbers

num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))
num3 = int(input("Enter num3 "))

if num1 > num2 and num1 > num3:
    print(f"num1 {num1} is maximum")
elif num2 > num1 and num2 > num3:
    print(f"num2 {num2} is maximum")
else:
    print(f"num3 {num3} is maximum")
