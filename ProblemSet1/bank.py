def main():
    greet = (input("Greetings")).split()
    print(value(greet))


def value(a):
    if a[0].lower()=='hello':
        return"$100"
    elif a[0].lower().startswith("h") and a[0].lower() != 'hello':
        return"$20"
    else:
        return"$0"


if __name__ == "__main__":
    main()
