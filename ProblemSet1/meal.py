def main():
    convert(time)
def convert(time):
    time = time.split(":")
    r = int(int(time[0])+(int(time[1])/60))
    if r >= 7 and r<=8:
        print ("breakfast time")
    elif r >= 12 and r<=13:
        print ("lunch time")
    elif r >= 18 and r<=19:
        print ("dinner time")
time = input("Time")
if __name__ == "__main__":
    main()

