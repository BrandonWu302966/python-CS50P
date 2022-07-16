def convert(ask):
    ask = ask.replace(":)","🙂")
    ask = ask.replace(":(","🙁")
    return(ask)
def main():
    ask = input("how do you feel")
    print(convert(ask))
main()
