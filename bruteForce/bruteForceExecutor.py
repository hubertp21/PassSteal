from . import bruteForceRandomLength
from . import bruteForceExactLength


def executeBruteForceAlgorithm(password, seconds):
    enable_exact_length_guessing = input("Do you want to enable exact length guessing? (y/n) ")
    if enable_exact_length_guessing == "y":
        print("Exact length guessing enabled")
        executeBruteForceForPasswordTypeAndLength(password, seconds)
    else:
        print("Exact length guessing disabled")
        executeBruteForceForPasswordType(password, seconds)


def executeBruteForceForPasswordTypeAndLength(password, seconds):
    print(f"Executing brute force algorithm on password: {password}")
    if password == password.lower():
        bruteForceExactLength.executeForLowercaseLettersExactLength(password, seconds)
    elif password == password.upper():
        bruteForceExactLength.executeForUppercaseLettersExactLength(password, seconds)
    elif password.isalpha():
        bruteForceExactLength.executeForLettersExactLength(password, seconds)
    elif password.isalnum():
        bruteForceExactLength.executeForAlphanumericsExactLength(password, seconds)
    else:
        bruteForceExactLength.executeForRandomsExactLength(password, seconds)


def executeBruteForceForPasswordType(password, seconds):
    print(f"Executing brute force algorithm on password: {password}")
    if password == password.lower():
        bruteForceRandomLength.executeForLowercaseLetters(password, seconds)
    elif password == password.upper():
        bruteForceRandomLength.executeForUppercaseLetters(password, seconds)
    elif password.isalpha():
        bruteForceRandomLength.executeForLetters(password, seconds)
    elif password.isalnum():
        bruteForceRandomLength.executeForAlphanumerics(password, seconds)
    else:
        bruteForceRandomLength.executeForRandoms(password, seconds)
