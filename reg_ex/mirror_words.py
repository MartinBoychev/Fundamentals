import re


def extract_word_pairs(text):
    pattern = r"(?P<delimiter>[@|#])(?P<word_one>[A-Za-z]{3,})(?P=delimiter){2}(?P<word_two>[A-Za-z]{3,})(?P=delimiter)"
    return [match.group(0) for match in re.finditer(pattern, text)]


def solve(text):
    word_pairs = extract_word_pairs(text)
    mirrored_pairs = []
    for pair in word_pairs:
        delimiter = pair[0]
        words = pair[1:-1].split(delimiter*2)
        if words[0] == words[1][::-1]:
            mirrored_pairs.append(words)

    if not word_pairs:
        print("No word pairs found!")
        print("No mirror words!")
        return

    print(f"{len(word_pairs)} word pairs found!")
    if not mirrored_pairs:
        print("No mirror words!")
        return
    print("The mirror words are:")
    print(", ".join([f"{pair[0]} <=> {pair[1]}" for pair in mirrored_pairs]))


text = input()
solve(text)
