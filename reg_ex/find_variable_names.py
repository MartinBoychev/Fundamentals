import re

input_str = input()
pattern = r'(^|(?<= ))_(?P<text>([A-Za-z]+))($|(?= ))'

matches = re.findall(pattern, input_str)

print(",".join(matches))
