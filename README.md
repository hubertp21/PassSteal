# Password Cracker

This Python program attempts to find a specified password using two techniques: **brute force** and **dictionary attack**. The program is designed to simulate a password guessing scenario, demonstrating how different algorithms can be used to crack passwords within a defined time limit.

## Features

- **Brute Force**: This method generates all possible combinations of characters to guess the password.
- **Dictionary Attack**: This method uses a predefined list of common passwords and variations to attempt to guess the password.
- **Unit Testing**: The program includes unit tests that verify the functionality of the password guessing algorithms using `unittest`.

## Requirements

- Python 3.x
- Required packages (if any) can be installed via `pip` (see `requirements.txt` if available).

## Usage

To run the program, use the command line with the following syntax:
```sh
python main.py <password> <time> <algorithm>
```
### Arguments

- `<password>`: The target password to guess (must be between 8 and 16 characters).
- `<time>`: The time in seconds the program will attempt to guess the password (must be greater than 10 seconds).
- `<algorithm>`: The algorithm to use for guessing the password. Valid options are:
  - `bruteForce`
  - `dictionaryAttack`

### Example

To run the program with a password of "mypassword", for 30 seconds using the brute force method:
```shell
python password_cracker.py mypassword 30 bruteForce
```

## Code Overview

The main class of the program is structured as follows:

```python
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
```
ENJOY