import sys
from bruteForce import bruteForceExecutor
from dictionaryAttack import dictionaryAttackExecutor


def main():
    if len(sys.argv) != 4:
        print("Program needs three arguments: password, time for resolving and algorithm type")
        exit(1)

    PASSWORD = sys.argv[1]

    if len(PASSWORD) < 8 or len(PASSWORD) > 16:
        print("Password must be at least 8 characters and not more than 16")
        exit(1)

    TIME = int(sys.argv[2])

    if TIME < 10:
        print("Time must be more than 10 seconds")
        exit(1)

    ALGORITHM = sys.argv[3]

    if ALGORITHM == "bruteForce":
        bruteForceExecutor.executeBruteForceAlgorithm(PASSWORD, TIME)
    elif ALGORITHM == "dictionaryAttack":
        dictionaryAttackExecutor.executeDictionaryAttackAlgorithm(PASSWORD, TIME)
    else:
        print("Wrong algorithm name provided")
        exit(1)


if __name__ == "__main__":
    main()
