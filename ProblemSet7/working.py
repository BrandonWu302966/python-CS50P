import re
import sys


def main():
    l = convert(input("Hours: ").strip())
    print(l)

def convert(s):
    if match := re.search("([0-1]?[0-9]):?([0-5][0-9])? (PM|AM) to ([0-1]?[0-9]):?([0-5][0-9])? (PM|AM)",s):
        if int(match.group(1)) > 12:
            raise ValueError
        if int(match.group(4)) > 12:
            raise ValueError
        try:
            startm = int(match.group(2))
        except TypeError:
            startm = "00"
        else:
            if startm == 0:
                startm = '00'
        try:
            endm = int(match.group(5))
        except TypeError:
            endm = "00"
        else:
            if endm == 0:
                endm = '00'
        if match.group(3) == "PM" and int(match.group(1)) != 12:
            starth = (int(match.group(1)) + 12)
        else:
            starth = int(match.group(1))
        if match.group(3) == "PM" and starth == 24 or match.group(3) == "AM" and starth == 12:
            starth = 0
        if match.group(6) == "PM" and int(match.group(4)) != 12:
            endh = (int(match.group(4)) + 12)
        else:
            endh = int(match.group(4))
        if match.group(6) == "PM" and endh == 24 or match.group(6) == "AM" and endh == 12:
            endh = 0
        if starth < 10:
            starth = f'0{starth}'
        if endh < 10:
            endh = f'0{endh}'
        return (f"{starth}:{startm} to {endh}:{endm}")
    else:
        raise ValueError



if __name__ == "__main__":
    main()