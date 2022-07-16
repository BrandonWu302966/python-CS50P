list = []
rlist=[]
while True:
    try:
        a = input("")
    except EOFError:
        break
    else:
        rlist.append(a)
        if a not in list:
            list.append(a)
        pass
for i in sorted(list):
    print(f"{rlist.count(i)} {i.upper()}")

