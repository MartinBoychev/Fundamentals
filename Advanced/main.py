try:
    with open('text.txt', 'r') as file:
        lines = file.readlines()

        for i in range(0, len(lines), 2):
            # Replace specified characters with "@"
            processed_line = lines[i].replace("-", "@").replace(",", "@").replace(".", "@").replace("!", "@").replace("?", "@")

            # Reverse the order of words
            words = processed_line.strip().split()
            reversed_line = ' '.join(reversed(words))

            print(reversed_line)

except FileNotFoundError:
    print("File not found: text.txt")
except Exception as e:
    print(f"An error occurred: {e}")
