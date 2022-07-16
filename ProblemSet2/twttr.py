import string
vowels = ["a","e","i","o","u","A","E","I","O","U"]
punctuations = string.punctuation
nums = ['0','1','2','3','4','5','6','7','8','9']
def main():
    print(shorten(input("phrase: ")))


def shorten(a):
    for i in vowels:
        a = a.replace(i, '')
    for j in punctuations:
        a = a.replace(j, '')
    for z in nums:
        a = a.replace(z, '')
    return(a)

if __name__ == "__main__":
    main()