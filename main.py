import random
from string import digits, punctuation, ascii_letters


SYMBOLS = ascii_letters + digits + punctuation


def generate_new_password(psd_range: int) -> str:
    secure_random = random.SystemRandom()
    return "".join(secure_random.choice(SYMBOLS) for i in range(psd_range))


print(generate_new_password(20))
