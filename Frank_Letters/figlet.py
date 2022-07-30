import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
if len(sys.argv) == 1:
    random_font = 1
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '-font'):
    random_font = 0
else:
    print('Invalid Usage')
    sys.exit(1)


if random_font == 1:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
elif random_font == 0:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print('Invalid Usage')
        sys.exit(1)

input_string = input('Input: ')
print('Output: ')
print(figlet.renderText(input_string))