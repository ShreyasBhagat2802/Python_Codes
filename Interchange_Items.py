string_list = ["Google", "TCS", "Accenture", "Apexon"]

print(string_list) 

first_item = string_list[0]
last_item = string_list[-1]

string_list[0] = last_item
string_list[-1] = first_item

print(string_list)