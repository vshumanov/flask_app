import random
domains = ["hotmail.com", "gmail.com", "aol.com",
           "mail.com", "mail.bg", "yahoo.com"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]


def get_random_domain():
    return random.choice(domains)


def get_random_name():
    _name = ""
    for _ in range(7):
        _name += random.choice(letters)
    return _name


def generate_random_email():
    return f'{get_random_name()}@{get_random_domain()}'
