import sys
import requests
if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)
elif len(sys.argv) == 2:
    try:
        num = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    y = r.json()
    if num == 1:
        result = y['bpi']['USD']['rate_float']
        print(f"${result:,.4f}")
    else:
        result = num * (y['bpi']['USD']['rate_float'])
        print(f"${result:,.4f}")
except requests.RequestException:
    print("Can not convert to bitcoin")
    sys.exit(1)