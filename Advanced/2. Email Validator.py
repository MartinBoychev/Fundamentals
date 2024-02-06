class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ["com", "bg", "net", "org"]

email = input()
while email != "End":
    if email.count("@") < 1:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(email.split("@")[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif email.split(".")[-1] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")

    email = input()
