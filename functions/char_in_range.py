# Write a function that receives two characters and returns a single string with all the characters in between them (
# according to the ASCII code), separated by a single space. Print the result on the console.

def print_ascii_numbers(start_char, end_chars):
    start_char = ord(start_char)
    end_chars = ord(end_chars)
    for num in range(start_char + 1, end_chars):
        print(chr(num), end=" ")


start = input()
end = input()
print_ascii_numbers(start, end)
