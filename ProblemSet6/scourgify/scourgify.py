import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
try:
    f = open(sys.argv[1])
    f = csv.DictReader(f)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
students = []
for row in f:
    last, first, house = row['name'].split(',')[0], row['name'].split(',')[1], row['house']
    students.append({'first': first.strip(), 'last': last.strip(), 'house': house.strip()})
with open(sys.argv[2], 'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["first", "last", "house"])
    for i in students:
        writer.writerow([f"{i['first']}",f"{i['last']}",f"{i['house']}"])



