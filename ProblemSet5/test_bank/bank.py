

def main():
    greet = input("Greetings")
    print(value(greet))


def value(a):
    a = a.split()
    if a[0].lower().strip(",")=='hello':
        return"$0"
    elif a[0].lower().startswith("h") and a[0].lower() != 'hello':
        return"$20"
    else:
        return"$100"


if __name__ == "__main__":
    main()