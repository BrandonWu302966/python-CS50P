import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(" um",' '+s,re.IGNORECASE)
    return len(match)



if __name__ == "__main__":
    main()