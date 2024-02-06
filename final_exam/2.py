import re

string = input()

pattern = r'([@|#]+)([a-z]{3,})([@|#]+)([^A-Za-z0-9])*/(\d+)/+'


matches = re.findall(pattern, string)

for match in matches:
    color = match[1]
    amount = match[4]
    print(f"You found {amount} {color} eggs!")
