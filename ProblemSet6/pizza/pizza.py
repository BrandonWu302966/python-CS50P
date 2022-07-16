import sys
from tabulate import tabulate

list = []
table = []
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    if '.csv' not in sys.argv[1]:
        sys.exit("Not a CSV file")
for i in file:
    list.append(i)

for b in list[1:]:
    b = b.split(',')
    table.append(b)
headers = list[0].rstrip('\n').split(',')
print(tabulate(table, headers, tablefmt = "grid"))