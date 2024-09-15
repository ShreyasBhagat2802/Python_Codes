#program to count number of vowels using sets in given string
string = str(input("Enter the string "))
print(string)
vowels = "AEIOUaeiou"

new_set = set(string)
print(new_set)
count_set = set()
count = 0
for element in new_set:
    for vowel in vowels:
        if element == vowel:
            count += 1
            count_set.add(element)
print(count_set)
print(count)