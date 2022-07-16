menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
bill = 0
while True:
    try:
        order = (input("Item: "))
    except EOFError:
        break
    else:
        o = []
        order = order.split()
        for i in order:
            i = i.capitalize()
            o.append(i)
        order = ' '.join(str(f) for f in o)
        if order in menu:
            bill = bill + float(menu[order])
            check = "{:.2f}".format(bill)
            print(f"Total: ${check}")
        else:
            pass
