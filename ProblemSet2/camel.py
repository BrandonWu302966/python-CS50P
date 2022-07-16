camelcase = (input("camelCase:")).strip()
list=[]
for i in camelcase:
    if i.isupper():
        i = f" {i}"
    list.append(i)
english = ''.join(str(i) for i in list)
snake = ((english.strip()).replace(' ','_')).lower()
print(snake)