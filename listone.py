my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
list1 = [];
for i in my_list[:]:
    if i not in list1:
        list1.append(i)
    
print("The list with unique elements only:")
print(list1)

