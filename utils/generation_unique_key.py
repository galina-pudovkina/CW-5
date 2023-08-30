from random import choice
from string import ascii_uppercase


def generate_unique_key(existings_vlaue: list):
    alphabet = ascii_uppercase
    while True:
        unique_key = "".join([choice(alphabet) for _ in range(4)])
        if unique_key not in existings_vlaue:
            existings_vlaue.append(unique_key)
            return unique_key
