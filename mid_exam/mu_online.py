import re
def NumberSearch(strParam):
    nums = re.findall(r'\d+', strParam)
    sum_nums = sum(int(n) for n in nums)
    num_letters = sum(1 for c in strParam if c.isalpha())
    avg_num = round(sum_nums / num_letters)
    return avg_num

print(NumberSearch(input()))