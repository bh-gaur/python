# dict = {"name" : "bhola",
#         "age" : 19,
#         "weight" : 50.20,
#         "programming languages" : ["python", "C"],
#         34 : ("test", "python"),
#         "subjects" : {    #nested dictonary
#             "phy" : 98,
#             "chem" : 95,
#             "maths" : 99
#         }
#     }

# print(dict)
# print(dict["name"])
# dict["age"] = 23 
# print("\n",dict)

# dict["college year"] = "2nd" #add new key value and can assign new value to key

# print(dict["subjects"]["maths"])
# print("\n",dict)
# print(dict.keys()) #returns all keys
# print(len(dict.keys())) #returns length of keys in dictonary

# print(dict.values()) #returns all values
# print(len(dict.values()))  #returns length of values in dictonary


# print(dict.items()) #return all key value pair
 
# print(dict["name2"]) # gives error and next code will not execute
# print(dict.get("name2")) #return none and next code will execute not stop (real scenario)


# dict2 = {"city" : "delhi", "course" : "Btech"}
# dict.update({"city":"delhi"}) #dict.update(dict2)
# print(dict)



# set = {1, (1.2, "test"), 1, 5, "hello"}   #we can store list and dict in set bcoz they are mutable
# print(type(set))
# print(list(set)) #convert set into list
# print(tuple(set)) #convert set into tuple
# print(len(set)) #number of items in set

# set1 = set #empty set
# print(set.add("learning")) #returns none and add element in set
# set.add("python")  #add element in set
# set.add("python")  #add element in set
# set.add((1, 2, 3))   #add tuple in set
# set.add([1, 2, 3])  #retruns error 

# set.remove(5) #removes 5 from set
# set.remove(34) #returns error
# set.discard(34) #returns none and next still running

# print(99 in set) #check 99 present or not in set
# set.clear() #empty the set
# x = set.pop() #removes random item form set
# print(x)

# print(set)


# set_first = {1, 2, 3, 4}
# set_second = {4, 5, 6, 7}

# print(set_first.union(set_second)) #returns union or combines the both set
# print(set.intersection(set_second)) #sreturns ame elements both both sets



#Q1
# dictonary = {
#     "table" : ["a piece of furniture", "list of facts & figures"],
#     "cat" : "a small animal"
# }

# print(dictonary)

#Q2
# students = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}

# classrooms = len(students)
# print(f"Total classrooms required are {classrooms} for all students")

#Q3
# marks = {}

# marks.update({"physics" : int(input("enter physics marks: ")),
#               "chemistry": int(input("enter chemisry marks: ")),
#               "maths": int(input("enter maths marks: "))
#             }
#            )

# x = int(input("enter physics marks: "))
# marks.update({"phy": x})

# x = int(input("enter chemistry marks: "))
# marks.update({"chem": x})

# x = int(input("enter maths marks: "))
# marks.update({"maths": x})

# print(marks)
