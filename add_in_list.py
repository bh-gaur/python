list_name=[]

list_name.insert(0, 5)
list_name.insert(1, 10)
list_name.insert(0, 6)

print(list_name)
# Output: [6, 5, 10]

list_name.remove(6)
list_name.insert(0, 1)
list_name.insert(2 ,9)

print(list_name)
# Output: [1, 5, 9, 10]

list_name.remove(10)
list_name.sort(reverse=True)
print(list_name)
# Output: [9, 5, 1]