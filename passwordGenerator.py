import string
import random

common_passwords = ["password", "password123", "letmein", "qwerty", "123456", "abc123", "admin", "welcome",
                    "monkey", "sunshine", "root", "toor", "abcdefgh", "12345678", "Password", "Password1"]
password_variations = ["", "1", "12", "111" "123", "1234", "12345", "123456", ".", "!", "@", "#", "$", "%", "^", "&", "*",
                       "(", ")", "-",
                       "_", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "<", ">"]


def generateDefaultRandomPassword():
    length = random.randint(8, 16)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generateRandomLowercaseLettersPassword():
    length = random.randint(8, 16)
    characters = string.ascii_lowercase
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generateRandomUppercaseLettersPassword():
    length = random.randint(8, 16)
    characters = string.ascii_uppercase
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generateRandomLettersPassword():
    length = random.randint(8, 16)
    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generateRandomAlphanumericPassword():
    length = random.randint(8, 16)
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generateDefaultRandomPasswordForExactLength(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generateRandomLowercaseLettersPasswordForExactLength(length):
    characters = string.ascii_lowercase
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generateRandomUppercaseLettersPasswordForExactLength(length):
    characters = string.ascii_uppercase
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generateRandomLettersPasswordForExactLength(length):
    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generateRandomAlphanumericPasswordForExactLength(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generateAllPasswordVariationsForDictionaryAttack():
    possible_passwords = list()
    for password in common_passwords:
        for variation in password_variations:
            possible_passwords.append(password + variation)
    return possible_passwords


def generatePasswordVariationsWithExactLengthForDictionaryAttack(length):
    possible_passwords = list()
    for password in common_passwords:
        for variation in password_variations:
            if len(password + variation) == length:
                possible_passwords.append(password + variation)
    return possible_passwords
