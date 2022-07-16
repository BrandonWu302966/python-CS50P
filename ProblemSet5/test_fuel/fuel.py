

def main():
    f = input("Fraction: ")
    convert(f)
    if "%" in convert(f):
        print(gauge(convert(f)))


def convert(exp):
    try:
        exp = exp.split('/')
        f = int(exp[0])/int(exp[1]) *100
    except ZeroDivisionError:
        return ZeroDivisionError
    except ValueError:
        return ValueError
    else:
        l = "{:.0f}".format(f)
        return (f"{l}%")

def gauge(p):
    if int(p.strip("%")) <= 100 and int(p.strip("%")) >= 99:
        return('F')
    elif int(p.strip("%")) <= 1:
        return('E')
    else:
        return(p)

if __name__ == "__main__":
    main()