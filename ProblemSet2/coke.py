c = 50
print(f"Amount Due: {c}" )
coins = ['5','10','25','50']
while True:
    i = input("Insert Coin: ")
    if i in coins:
        c = c - int(i)
    if c <= 0:
        print(f"Change Owed: {c*-1}")
        break
    else:
        print(f"Amount Due: {c}")