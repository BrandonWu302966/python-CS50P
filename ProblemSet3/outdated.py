months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def formed(a):
    if len((str(a)).strip()) == 2:
        return a
    else:
        return (f"0{str(a).strip()}")
while True:
    unform = input("Date: ")
    unform = unform.strip()
    if '/' in unform:
        unform = unform.split('/')
        try:
            int(unform[0]) - 1
            month = months[int(unform[0])]
        except IndexError:
            pass
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            if int(unform[1]) > 31:
                pass
            else:
                print(f"{unform[2]}-{formed(unform[0])}-{formed(unform[1])}")
                break
    elif ',' in unform:
        unform = unform.split()
        if unform[0] in months:
            month = months.index(unform[0]) + 1
            day = unform[1].strip(',')
            if int(day) > 31:
                pass
            else:
                print(f"{unform[2]}-{formed(month)}-{formed(day)}")
                break
        else:
            pass
    else:
        pass
