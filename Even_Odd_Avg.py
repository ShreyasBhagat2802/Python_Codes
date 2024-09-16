list = [3,5,7,2,8,9]

even = 0
count1 = 0
odd = 0
count2 = 0


for i in list:
    if i % 2 == 0:
        even += i
        count1 += 1
    else:
        odd += i
        count2 += 1

print(even/count1)
print(odd/count2)
