my_list = [1, "hello", 3.14, True, "world", 42, None, "Python"]
string_count = 0
for element in my_list:
    if type(element) == str:
        string_count += 1
print("Number of string elements:", string_count)
