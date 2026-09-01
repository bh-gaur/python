import csv

with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 25, 'New York'])
    writer.writerow(['Bob', 30, 'Los Angeles'])
    writer.writerow(['Charlie', 35, 'Chicago'])

print("Created data.csv with sample data.")

with open('data.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)