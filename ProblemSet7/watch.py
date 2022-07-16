import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if match := re.search('src="https?://(www\.)?youtube\.com/embed/(\w+)"(.+)?$', s):
        return f"https://youtu.be/{match.group(2)}"





if __name__ == "__main__":
    main()