phrase = input("Please write your phrase")
phrase = phrase.split()
new = "...".join(str(i) for i in phrase)
print (new)