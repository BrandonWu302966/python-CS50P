from random import randint


def main():
    print(generate_integer(get_level()))


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if int(level) in range(1,4):
                break
            else:
                pass
    return level

def generate_integer(level):
    c = 0
    i = 10
    while i > 0:
        if level == 1:
            X = randint(0,9)
            Y = randint(0,9)
        elif level == 2:
            X = randint(10,99)
            Y = randint(10,99)
        elif level == 3:
            X = randint(100,999)
            Y = randint(100,999)
        Ec = 0
        ans = X + Y
        exp = (f"{X} + {Y}")
        while True:
            if Ec == 3:
                print(ans)
                i -=1
                break
            try:
                res = int(input(f"{exp} = "))
            except ValueError:
                print("E"*3)
                Ec += 1
                pass
            else:
                if res == ans:
                    if Ec == 0:
                        c +=1
                    i -=1
                    break
                else:
                    Ec += 1
                    print("E"*3)
                    pass

    return (f"Score: {c}")


if __name__ == "__main__":
    main()
