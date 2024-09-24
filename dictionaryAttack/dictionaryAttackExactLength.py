import time
import passwordGenerator


def executeForExactLength(password, seconds):
    start_time = time.time()
    length = len(password)
    possible_passwords = passwordGenerator.generatePasswordVariationsWithExactLengthForDictionaryAttack(length)
    while (time.time() - start_time) < seconds:
        for possible_password in possible_passwords:
            if possible_password == password:
                print(f"Password: {password} guessed! Password generated: {possible_password}")
                return
            print(f"Wrong guess. Generated password: {possible_password}")
    print(f"Time has exceeded. Password not guessed :(")
