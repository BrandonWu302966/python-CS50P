list = []
while True:
    name = input("Name")
    if (name.lower()).strip() == 'done':
        break
    elif len(name.split()) != 2:
        print("Only First and Last name please")
    else:
        list.append(name)

list1 = []
for i in list:
    i = i.split()
    list1.append(i[0].title() + ' ' + i[1].title())
print (list1)