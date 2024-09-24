import time
import passwordGenerator


def executeForRandoms(password, seconds):
    start_time = time.time()
    while (time.time() - start_time) < seconds:
        generated_password = passwordGenerator.generateRandomLowercaseLettersPassword()
        if generated_password == password:
            print(f"Password: {password} guessed! Password generated: {generated_password}")
            return
        print(f"Wrong guess. Generated password: {generated_password}")
    print("Time has exceeded. Password not guessed :(")


def executeForLowercaseLetters(password, seconds):
    start_time = time.time()
    while (time.time() - start_time) < seconds:
        generated_password = passwordGenerator.generateRandomLowercaseLettersPassword()
        if generated_password == password:
            print(f"Password: {password} guessed! Password generated: {generated_password}")
            return
        print(f"Wrong guess. Generated password: {generated_password}")
    print("Time has exceeded. Password not guessed :(")


def executeForUppercaseLetters(password, seconds):
    start_time = time.time()
    while (time.time() - start_time) < seconds:
        generated_password = passwordGenerator.generateRandomUppercaseLettersPassword()
        if generated_password == password:
            print(f"Password: {password} guessed! Password generated: {generated_password}")
            return
        print(f"Wrong guess. Generated password: {generated_password}")
    print("Time has exceeded. Password not guessed :(")


def executeForLetters(password, seconds):
    start_time = time.time()
    while (time.time() - start_time) < seconds:
        generated_password = passwordGenerator.generateRandomLettersPassword()
        if generated_password == password:
            print(f"Password: {password} guessed! Password generated: {generated_password}")
            return
        print(f"Wrong guess. Generated password: {generated_password}")
    print("Time has exceeded. Password not guessed :(")


def executeForAlphanumerics(password, seconds):
    start_time = time.time()
    while (time.time() - start_time) < seconds:
        generated_password = passwordGenerator.generateRandomAlphanumericPassword()
        if generated_password == password:
            print(f"Password: {password} guessed! Password generated: {generated_password}")
            return
        print(f"Wrong guess. Generated password: {generated_password}")
    print("Time has exceeded. Password not guessed :(")
