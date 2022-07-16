fdict = [{'name': 'apple', 'calories':'130'},{'name': 'avocado', 'calories':'50'},{'name': 'sweet cherries', 'calories':'100'},{'name': 'kiwifruit', 'calories':'90'},{'name': 'pear', 'calories':'100'}]
while True:
    fruit = (input("fruit")).lower()
    for i in fdict:
        if fruit == i['name']:
            print(i['calories'])
            break
        else:
            continue
    break