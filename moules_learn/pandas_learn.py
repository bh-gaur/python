import pandas as pd

# Create a DataFrame
data = {"name": ["Alice","Bob", "Charlie"], "age": [25, 30, 35], "city": ["New York", "Los Angeles", "Chicago"]}
df = pd.DataFrame(data)

print("DataFrame created:")
# Display the DataFrame
print(df, "\n")
# Accessing specific columns
print(df["name"], "\n")
# Filtering rows based on a condition
print(df[df["age"] > 30])


print("\nDataFrame info:")
# Display DataFrame info
print(df.info(), "\n")

print("DataFrame description:")
# Display DataFrame description
print(df.describe(), "\n")

print(df[["name", "age"]])