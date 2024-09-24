import unittest
from unittest.mock import patch

from bruteForce import bruteForceExecutor


class BruteForceExecutorTest(unittest.TestCase):

    @patch('builtins.input', return_value='y')
    @patch('bruteForce.bruteForceExecutor.executeBruteForceForPasswordTypeAndLength')
    def test_execute_bruteforce_algorithm_exact_length_enabled(self, mock_execute_exact_length, mock_input):
        # given
        password = "password123"
        seconds = 20

        # when
        bruteForceExecutor.executeBruteForceAlgorithm(password, seconds)

        # then
        mock_input.assert_called_once_with("Do you want to enable exact length guessing? (y/n) ")
        mock_execute_exact_length.assert_called_once_with(password, seconds)

    @patch('builtins.input', return_value='n')
    @patch('bruteForce.bruteForceExecutor.executeBruteForceForPasswordType')
    def test_execute_bruteforce_algorithm_exact_length_disabled(self, mock_execute_random_length, mock_input):
        # given
        password = "password123"
        seconds = 20

        # when
        bruteForceExecutor.executeBruteForceAlgorithm(password, seconds)

        # then
        mock_input.assert_called_once_with("Do you want to enable exact length guessing? (y/n) ")
        mock_execute_random_length.assert_called_once_with(password, seconds)

    @patch('bruteForce.bruteForceExactLength.executeForLowercaseLettersExactLength')
    def test_execute_bruteforce_for_password_type_and_length_lowercase(self, mock_execute_lowercase):
        # given
        password = "password"
        seconds = 20

        # when
        bruteForceExecutor.executeBruteForceForPasswordTypeAndLength(password, seconds)

        # then
        mock_execute_lowercase.assert_called_once_with(password, seconds)

    @patch('bruteForce.bruteForceExactLength.executeForUppercaseLettersExactLength')
    def test_execute_bruteforce_for_password_type_and_length_uppercase(self, mock_execute_uppercase):
        # given
        password = "PASSWORD"
        seconds = 20

        # when
        bruteForceExecutor.executeBruteForceForPasswordTypeAndLength(password, seconds)

        # then
        mock_execute_uppercase.assert_called_once_with(password, seconds)

    @patch('bruteForce.bruteForceExactLength.executeForLettersExactLength')
    def test_execute_bruteforce_for_password_type_and_length_letters(self, mock_execute_letters):
        # given
        password = "Password"
        seconds = 20

        # when
        bruteForceExecutor.executeBruteForceForPasswordTypeAndLength(password, seconds)

        # then
        mock_execute_letters.assert_called_once_with(password, seconds)

    @patch('bruteForce.bruteForceExactLength.executeForAlphanumericsExactLength')
    def test_execute_bruteforce_for_password_type_and_length_alphanumeric(self, mock_execute_alphanumerics):
        # given
        password = "Password123"
        seconds = 20

        # when
        bruteForceExecutor.executeBruteForceForPasswordTypeAndLength(password, seconds)

        # then
        mock_execute_alphanumerics.assert_called_once_with(password, seconds)

    @patch('bruteForce.bruteForceExactLength.executeForRandomsExactLength')
    def test_execute_bruteforce_for_password_type_and_length_random(self, mock_execute_random):
        # given
        password = "P@ssw0rd!"
        seconds = 20

        # when
        bruteForceExecutor.executeBruteForceForPasswordTypeAndLength(password, seconds)

        # then
        mock_execute_random.assert_called_once_with(password, seconds)

    @patch('bruteForce.bruteForceRandomLength.executeForLowercaseLetters')
    def test_execute_bruteforce_for_password_type_lowercase(self, mock_execute_lowercase):
        # given
        password = "password"
        seconds = 20

        # when
        bruteForceExecutor.executeBruteForceForPasswordType(password, seconds)

        # then
        mock_execute_lowercase.assert_called_once_with(password, seconds)

    @patch('bruteForce.bruteForceRandomLength.executeForUppercaseLetters')
    def test_execute_bruteforce_for_password_type_uppercase(self, mock_execute_uppercase):
        # given
        password = "PASSWORD"
        seconds = 20

        # when
        bruteForceExecutor.executeBruteForceForPasswordType(password, seconds)

        # then
        mock_execute_uppercase.assert_called_once_with(password, seconds)

    @patch('bruteForce.bruteForceRandomLength.executeForLetters')
    def test_execute_bruteforce_for_password_type_letters(self, mock_execute_letters):
        # given
        password = "Password"
        seconds = 20

        # when
        bruteForceExecutor.executeBruteForceForPasswordType(password, seconds)

        # then
        mock_execute_letters.assert_called_once_with(password, seconds)

    @patch('bruteForce.bruteForceRandomLength.executeForAlphanumerics')
    def test_execute_bruteforce_for_password_type_alphanumeric(self, mock_execute_alphanumerics):
        # given
        password = "Password123"
        seconds = 20

        # when
        bruteForceExecutor.executeBruteForceForPasswordType(password, seconds)

        # then
        mock_execute_alphanumerics.assert_called_once_with(password, seconds)

    @patch('bruteForce.bruteForceRandomLength.executeForRandoms')
    def test_execute_bruteforce_for_password_type_random(self, mock_execute_random):
        # given
        password = "P@ssw0rd!"
        seconds = 20

        # when
        bruteForceExecutor.executeBruteForceForPasswordType(password, seconds)

        # then
        mock_execute_random.assert_called_once_with(password, seconds)


if __name__ == "__main__":
    unittest.main()
