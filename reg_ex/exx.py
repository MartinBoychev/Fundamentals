import re

text = input()

digits = re.findall(r'\d', text)
coolThresholdSum = 1
for digit in digits:
    coolThresholdSum *= int(digit)
print(f"Cool threshold: {coolThresholdSum}")

emojis = re.findall(r'(::|\*\*)([A-Z][a-z]{2,})\1', text)
coolEmojis = []
for emoji in emojis:
    coolness = sum(ord(char) for char in emoji[1])
    if coolness > coolThresholdSum:
        coolEmojis.append(emoji[0] + emoji[1] + emoji[0])

print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in coolEmojis:
    print(emoji)
