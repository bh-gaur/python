#continue statement

for i in range(1, 10):
    if i == 5:
        print("Skipping the value of i =", i)
        continue  # Skips the rest of the code when i == 5
        print("execution after continue") # this will not execute
    print(i)


#break statement
for i in range(1, 10):
    if i == 5:
        print("Skipping the value of i =", i)
        break  # Loop terminates when i == 5
        print("execution after continue") # this will not execute
    print(i)