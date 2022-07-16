import sys
import requests

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
bpi = ((r.json()["bpi"])['USD'])['rate_float']


try:
    float(sys.argv[1])
except ValueError:
    sys.exit(f"{sys.argv[1]} is not a number")
except IndexError:
    sys.exit("Missing command_line argument")
else:
    amt = float(sys.argv[1])

conv = amt*bpi

print(f"${conv:,.4f}")
