# print the table 

x = int(input())       # Take input from user 

print("The table of", x)

for i in range(1,11):
    print(x,"x",i,"=",x*i)
    
def table(n):
  for i in range(1,11):
    print(n*i)


for i in range(1,11):
  table(i)
