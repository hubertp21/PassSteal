import unittest
from unittest.mock import patch

from bruteForce import bruteForceExactLength


class BruteForceExactLengthTest(unittest.TestCase):

    @patch('passwordGenerator.generateDefaultRandomPasswordForExactLength')
    @patch('time.time', side_effect=[0, 1, 2, 3, 4])
    def test_execute_for_randoms_exact_length_guessed(self, mock_time, mock_generate_password):
        # given
        mock_generate_password.return_value = 'password123'
        password = 'password123'
        seconds = 5

        # when
        with patch('builtins.print') as mock_print:
            bruteForceExactLength.executeForRandomsExactLength(password, seconds)

        # then
        mock_print.assert_any_call(f"Password: {password} guessed! Password generated: {password}")
        mock_generate_password.assert_called_with(len(password))

    @patch('passwordGenerator.generateRandomLowercaseLettersPasswordForExactLength')
    @patch('time.time', side_effect=[0, 1, 2, 3, 4])
    def test_execute_for_lowercase_letters_exact_length_guessed(self, mock_time, mock_generate_password):
        # given
        mock_generate_password.return_value = 'password'
        password = 'password'
        seconds = 5

        # when
        with patch('builtins.print') as mock_print:
            bruteForceExactLength.executeForLowercaseLettersExactLength(password, seconds)

        # then
        mock_print.assert_any_call(f"Password: {password} guessed! Password generated: {password}")
        mock_generate_password.assert_called_with(len(password))

    @patch('passwordGenerator.generateRandomUppercaseLettersPasswordForExactLength')
    @patch('time.time', side_effect=[0, 1, 2, 3, 4])
    def test_execute_for_uppercase_letters_exact_length_guessed(self, mock_time, mock_generate_password):
        # given
        mock_generate_password.return_value = 'PASSWORD'
        password = 'PASSWORD'
        seconds = 5

        # when
        with patch('builtins.print') as mock_print:
            bruteForceExactLength.executeForUppercaseLettersExactLength(password, seconds)

        # then
        mock_print.assert_any_call(f"Password: {password} guessed! Password generated: {password}")
        mock_generate_password.assert_called_with(len(password))

    @patch('passwordGenerator.generateRandomLettersPasswordForExactLength')
    @patch('time.time', side_effect=[0, 1, 2, 3, 4])
    def test_execute_for_letters_exact_length_guessed(self, mock_time, mock_generate_password):
        # given
        mock_generate_password.return_value = 'abcDEF'
        password = 'abcDEF'
        seconds = 5

        # when
        with patch('builtins.print') as mock_print:
            bruteForceExactLength.executeForLettersExactLength(password, seconds)

        # then
        mock_print.assert_any_call(f"Password: {password} guessed! Password generated: {password}")
        mock_generate_password.assert_called_with(len(password))

    @patch('passwordGenerator.generateRandomAlphanumericPasswordForExactLength')
    @patch('time.time', side_effect=[0, 1, 2, 3, 4])
    def test_execute_for_alphanumerics_exact_length_guessed(self, mock_time, mock_generate_password):
        # given
        mock_generate_password.return_value = 'abc123DEF'
        password = 'abc123DEF'
        seconds = 5

        # when
        with patch('builtins.print') as mock_print:
            bruteForceExactLength.executeForAlphanumericsExactLength(password, seconds)

        # then
        mock_print.assert_any_call(f"Password: {password} guessed! Password generated: {password}")
        mock_generate_password.assert_called_with(len(password))

    @patch('passwordGenerator.generateDefaultRandomPasswordForExactLength')
    @patch('time.time', side_effect=[0, 1, 2, 3, 10])
    def test_execute_for_randoms_exact_length_time_exceeded(self, mock_time, mock_generate_password):
        # given
        mock_generate_password.return_value = 'wrongPassword'
        password = 'password123'
        seconds = 5

        # when
        with patch('builtins.print') as mock_print:
            bruteForceExactLength.executeForRandomsExactLength(password, seconds)

        # then
        mock_print.assert_any_call("Time has exceeded. Password not guessed :(")
        mock_generate_password.assert_called_with(len(password))


if __name__ == "__main__":
    unittest.main()
