vowels = ["a","e","i","o","u","A","E","I","O","U"]
def main():
    print(shorten(input("phrase: ")))


def shorten(a):
    for i in vowels:
        a = a.replace(i, '')
    return(a)

if __name__ == "__main__":
    main()