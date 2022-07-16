from datetime import date
import sys
import re
import inflect

p = inflect.engine()

class Days:
    def __init__(self, bday, today):
        self.today = today
        self.bday = bday

    def __str__(self):
        return f"{self.timediff()} minutes"

    def timediff(self):
        convbday = date.fromisoformat(self.bday)
        ac = self.today
        diff = convbday - ac
        ddiff = str(diff).split(",")[0]
        nums = re.search (".?([0-9]+) days",ddiff)
        tmins = int(nums.group(1)) * 24 * 60
        return speech(tmins)


    @property
    def bday(self):
        return self._bday

    @bday.setter
    def bday(self, bday):
        if match := re.search("([0-9]{4})-([0-9]{2})-([0-9]{2})", bday):
            if int(match.group(2)) > 12:
                sys.exit("NO")
            if int(match.group(3)) > 31:
                sys.exit("NO")
        else:
            sys.exit("NO")
        self._bday = bday

def speech(n):
    return(p.number_to_words(n).capitalize().replace(" and",''))


def main():
    time = get_timetill()
    print(time)

def get_timetill():
    today = date.today()
    try:
        bday = str(input("Birthday: "))
    except ValueError:
        sys.exit
    timetill = Days(bday, today)
    return timetill


if __name__ == "__main__":
    main()

'''
When setting up class Days, I create the object Days and within class, I can determine the structure of the object
When setting up the function get_day(), I assign a value to the object and assign attributes to the object by using .hours or .mins (.)
I must return the object with its new attributes

When setting up class Days, I create the object Days and I create a structure for each object of the class. Initialize is the function that
prepares the class to be structured, self is the (object itself) and the placeholders of empty values are placed beside self. Within the function, I
must assign attributes to the placeholders.
'''