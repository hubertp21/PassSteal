import time
import passwordGenerator


def executeForRandomsExactLength(password, seconds):
    length = len(password)
    start_time = time.time()
    while (time.time() - start_time) < seconds:
        generated_password = passwordGenerator.generateDefaultRandomPasswordForExactLength(length)
        if generated_password == password:
            print(f"Password: {password} guessed! Password generated: {generated_password}")
            return
        print(f"Wrong guess. Generated password: {generated_password}")
    print("Time has exceeded. Password not guessed :(")


def executeForLowercaseLettersExactLength(password, seconds):
    length = len(password)
    start_time = time.time()
    while (time.time() - start_time) < seconds:
        generated_password = passwordGenerator.generateRandomLowercaseLettersPasswordForExactLength(length)
        if generated_password == password:
            print(f"Password: {password} guessed! Password generated: {generated_password}")
            return
        print(f"Wrong guess. Generated password: {generated_password}")
    print("Time has exceeded. Password not guessed :(")


def executeForUppercaseLettersExactLength(password, seconds):
    length = len(password)
    start_time = time.time()
    while (time.time() - start_time) < seconds:
        generated_password = passwordGenerator.generateRandomUppercaseLettersPasswordForExactLength(length)
        if generated_password == password:
            print(f"Password: {password} guessed! Password generated: {generated_password}")
            return
        print(f"Wrong guess. Generated password: {generated_password}")
    print("Time has exceeded. Password not guessed :(")


def executeForLettersExactLength(password, seconds):
    length = len(password)
    start_time = time.time()
    while (time.time() - start_time) < seconds:
        generated_password = passwordGenerator.generateRandomLettersPasswordForExactLength(length)
        if generated_password == password:
            print(f"Password: {password} guessed! Password generated: {generated_password}")
            return
        print(f"Wrong guess. Generated password: {generated_password}")
    print("Time has exceeded. Password not guessed :(")


def executeForAlphanumericsExactLength(password, seconds):
    length = len(password)
    start_time = time.time()
    while (time.time() - start_time) < seconds:
        generated_password = passwordGenerator.generateRandomAlphanumericPasswordForExactLength(length)
        if generated_password == password:
            print(f"Password: {password} guessed! Password generated: {generated_password}")
            return
        print(f"Wrong guess. Generated password: {generated_password}")
    print("Time has exceeded. Password not guessed :(")
