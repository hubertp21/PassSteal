from . import dictionaryAttackRandomLength
from . import dictionaryAttackExactLength


def executeDictionaryAttackAlgorithm(password, seconds):
    enable_exact_length_guessing = input("Do you want to enable exact length guessing? (y/n) ")
    if enable_exact_length_guessing == "y":
        print("Exact length guessing enabled")
        executeDictionaryAttackForPasswordLength(password, seconds)
    else:
        print("Exact length guessing disabled")
        executeDictionaryAttack(password, seconds)


def executeDictionaryAttackForPasswordLength(password, seconds):
    print(f"Executing brute force algorithm on password: {password}")
    dictionaryAttackExactLength.executeForExactLength(password, seconds)


def executeDictionaryAttack(password, seconds):
    print(f"Executing brute force algorithm on password: {password}")
    dictionaryAttackRandomLength.executeForRandomLength(password, seconds)