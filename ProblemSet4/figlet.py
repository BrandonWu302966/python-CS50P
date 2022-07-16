from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

accept = ["-f", "--font"]

if len(sys.argv[1]) == 1:
    i = input("Input: ")
    f = random.choice(figlet.getFonts())
    figlet.setFont(font = random.choice(figlet.getFonts()))
    print(figlet.renderText(i))
elif sys.argv[1] in accept:
    try:
            (figlet.getFonts()).index(sys.argv[2])
    except:
            sys.exit("Invalid usage")
    else:
            i = input("Input:")
            figlet.setFont(font = str(sys.argv[2]))
            print(figlet.renderText(i))
else:
    sys.exit("Invalid usage")