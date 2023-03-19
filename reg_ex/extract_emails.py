import re

string = input()

email_pattern = r'\s([A-Za-z0-9][\w\-.]*[A-Za-z0-9]@[A-Za-z][A-Za-z\-]*[A-Za-z](\.[A-Za-z][A-Za-z\-]*[A-Za-z])+)'
emails = re.findall(email_pattern, string)

print("\n".join(groups[0] for groups in emails))
