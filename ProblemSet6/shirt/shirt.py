import sys
from PIL import Image, ImageOps

ext = ['jpg','jpeg','png']
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
try:
    e1 = sys.argv[1].split('.')[1]
except IndexError:
    sys.exit("Invalid input")
else:
    if e1.lower() not in ext:
        sys.exit('Invalid input')
try:
    e2 = sys.argv[2].split('.')[1]
except IndexError:
    sys.exit("Invalid output")
else:
    if e1.lower() not in ext:
        sys.exit('Invalid output')

if sys.argv[2].split('.')[1].lower() != sys.argv[1].split('.')[1].lower():
    sys.exit("Input and output have different extensions")

im = Image.open(sys.argv[1])
with Image.open('shirt.png') as s:
    im = ImageOps.fit(im, size=s.size)
    shirt = ImageOps.fit(s, size=im.size)
    im.paste(shirt, shirt)
    im.save(sys.argv[2])

