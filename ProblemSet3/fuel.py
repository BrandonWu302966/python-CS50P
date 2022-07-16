while True:
    try:
        exp = input("Fraction: ")
        exp = exp.split('/')
        int(exp[0])/int(exp[1])
    except ZeroDivisionError:
        pass
    except ValueError:
        pass
    else:
        if float(exp[0]) / float(exp[1]) > 1:
            pass
        elif float(exp[0])/float(exp[1]) <= 1 and float(exp[0])/float(exp[1]) >= 0.99:
            print('F')
            break
        elif float(exp[0])/float(exp[1]) <= 0.01:
            print('E')
            break
        else:
            f = int(exp[0])/int(exp[1]) *100
            p = "{:.0f}".format(f)
            print(f"{p}%")
            break

