import sys

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")
except IndexError:
    sys.exit("Too few command-line arguments")
else:
    if '.py' not in sys.argv[1]:
        sys.exit("Not a python file")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        list = []
        i = 0
        for line in file:
            list.append(line.lstrip("\n' '"))
        for b in list:
            if b.startswith("#") or b == '':
                continue
            else:
                i+=1
        print(i)


