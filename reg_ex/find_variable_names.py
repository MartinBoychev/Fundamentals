import re

input_str = input()
pattern = r'\b\_[A-Za-z]+\b'

matches = re.findall(pattern, input_str)

print(",".join(matches).replace("_", ""))

