list= []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
    else:
        list.append(name)
if len(list) == 1:
    print(f"Adieu, adieu, to {', '.join(str(i) for i in list)}")
elif len(list) == 2:
    list[-1] = f"and {list[-1]}"
    print(f"Adieu, adieu, to {' '.join(str(i) for i in list)}")
else:
    list[-1] = f"and {list[-1]}"
    print(f"Adieu, adieu, to {', '.join(str(i) for i in list)}")
