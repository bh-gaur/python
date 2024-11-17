## Reading a file

# f = open("error.txt", "r")
# data = f.read()  #reads entire file
# # data = f.read(6)  #print starting 6 charcters
# print(data)

# # line1 = f.readline()  #reads one line at a time
# # print(line1)

# # line2 = f.readline()  #reads one line at a time
# # print(line2)

# f.close()


## Writing to a file

# f = open("error.txt", "w") #write mode
# f.write("This is a new line") #overwrites the entire file
# f.close()

# f = open("error.txt", "r")
# data = f.read()
# print(data)
# f.close()

# f = open("error.txt", "a") #append mode
# f.write("\nThis is a new line \nI am learning python from apna college")
# f.close()

# f = open("error.txt", "r")
# data = f.read()
# print(data)
# f.close()

## Create file
# f = open("sample.txt", "w") #open("sample.txt", "a")
# f.close()

## With syntax
# with open("sample.txt", "r") as f:  #read mode
#     print(f.read())

# with open("sample.txt", "w") as f:  #write mode
#     f.write("Testing with syntax in python")

## Deleting a file
# import os
# os.remove("error.txt")

# os.mkdir("test/bhola")
# os.rmdir("test/bhola")


### Create a new file "practice.txt" using python. Add following data in it

# with open("/Users/vishnu/learning/b_github/python-learn/practice.txt", "w") as f:  # or  with open("/Users/vishnu/learning/b_github/python-learn/practice.txt", "a") as f
#     f.write("Hi everyone \nwe are learning File I/O \nusing Java. \nI like programming in Java.")


### WAF that replace all occurences of "java" with "python" in above file.

# f = open("practice.txt", "r") 
# data = f.read()
# if "Java" in data:
#     new_data = data.replace("Java", "Python")
# f.close()

# f = open("practice.txt", "w")
# f.write(new_data)
# f.close()


# def replacing():
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if "Java" in data:
#             print(data.replace("Java", "Python"))
# replacing()


### Search if the word "learning" exists in the file or not

# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if (data.find(word)):
#         print(f"'{word}' word found")
#     else:
#         print("Not found")


### WAF to find in which line of the file does the word "learning" occur first. Print -1 if word not found.

# word = "Python"
# def find_line():
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no +=1
#     return -1

# print(find_line())


### From file containing numbers separated by comma, print the count of even numbers.

count = 0
with open("sample.txt", "r") as f:
    data = f.read()
    nums = list(data.split(","))
    for val in nums:
        if(int(val)%2 == 0):
            count += 1

print(count)