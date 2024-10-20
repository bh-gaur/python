# list = [45, 45.45, 67, 23] #list in python

# # list.append("test")
# print(list[0])
# print(list.sort())
# print(list.sort(reverse=True))
# print(list.reverse())
# print(list.insert(1,4)) 
# print(list.remove(45.45))
# print(list.pop(1))
# print(list)
# print(list.index(67))


# tup = (2, 1, 4, 3, 1, 5) #tuple in python
# tup1 = ()  #empty tuple
# tup2 = (1,) #single element tuple
# print(type(tup))
# print(tup[4])
# print(tup[1:4])
# print(tup.index(4))
# print(tup.count(1))


              ###WAP to ask the user to enter names of their 3 favourite movies & store them in a list

# list = []

# list.append(input("enter your first favourite movie name: "))
# list.append(input("enter your second favourite movie name: "))
# list.append(input("enter your third favourite movie name: "))

# first = input("enter your first favourite movie name: ")
# second = input("enter your second favourite movie name: ")
# third = input("enter your third favourite movie name: ")
# list = [first, second, third]

# list.append(first)
# list.append(second)
# list.append(third)
# print(list)



                  ###WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)

# list1 = [1, 2, 3, 2, 1] #palindrome
# list1 = [1, 2, 3, 2, 2] #NOT palindrome

# list2 = list1.copy()
# list2.reverse()


# if(list1 == list2):
#     print("palindrome")
# else:
#     print("NOT palindrome")

#                   ###WAP to count the numbers of students with the "A" grade in the following tuple
# test = ("C", "D", "A", "A", "B", "B", "A")

# print(test.count("A"))

#                   ###Store the above values in aclist & sort them from "A" to "D"
# list1 = list(test)
# print(type(list1))     

# list1.sort()
# print(list1)
