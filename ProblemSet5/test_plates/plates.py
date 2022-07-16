import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) <2 or len(s) > 6:
        return False
    for l in s:
        if l in string.punctuation:
            return False
    try:
        int(s[0])
    except ValueError:
        try:
            int(s[1])
        except ValueError:
            pass
        else:
            return False
    else:
        return False
    c = 0
    for l in s:
        if l.isdigit() and c == 0 and int(l) == 0:
            c += 1
            return False
        elif l.isdigit() and c == 0 and int(l) != 0:
            c += 1
            continue
    t = list()
    for l in s:
        if l.isdigit():
            t.append(l)
    b = 0
    for l in s:
        try:
            int(l)
        except ValueError:
            if b == 0:
                pass
            else:
                return False
        else:
            b += 1
    for l in s:
        if l.isdigit():
            if s[-1].isdigit():
                continue
            else:
                return False
    return True


if __name__ == '__main__':
    main()