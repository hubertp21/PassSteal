import unittest
from unittest.mock import patch

from bruteForce import bruteForceRandomLength


class BruteForceRandomLengthTest(unittest.TestCase):

    @patch('passwordGenerator.generateRandomLowercaseLettersPassword')
    @patch('time.time', side_effect=[0, 5, 10, 15, 20, 25])
    def test_execute_for_randoms_guesses_password(self, mock_time, mock_generate):
        # given
        mock_generate.side_effect = ['wrong_pass', 'password123']
        password = 'password123'
        seconds = 30

        # when
        bruteForceRandomLength.executeForRandoms(password, seconds)

        # then
        mock_generate.assert_called()
        self.assertEqual(mock_generate.call_count, 2)

    @patch('passwordGenerator.generateRandomLowercaseLettersPassword')
    @patch('time.time', side_effect=[0, 5, 10, 15, 20, 25])
    def test_execute_for_lowercase_letters_guesses_password(self, mock_time, mock_generate):
        # given
        mock_generate.side_effect = ['wrong_pass', 'password123']
        password = 'password123'
        seconds = 30

        # when
        bruteForceRandomLength.executeForLowercaseLetters(password, seconds)

        # then
        mock_generate.assert_called()
        self.assertEqual(mock_generate.call_count, 2)

    @patch('passwordGenerator.generateRandomUppercaseLettersPassword')
    @patch('time.time', side_effect=[0, 5, 10, 15, 20, 25])
    def test_execute_for_uppercase_letters_guesses_password(self, mock_time, mock_generate):
        # given
        mock_generate.side_effect = ['WRONG_PASS', 'PASSWORD123']
        password = 'PASSWORD123'
        seconds = 30

        # when
        bruteForceRandomLength.executeForUppercaseLetters(password, seconds)

        # then
        mock_generate.assert_called()
        self.assertEqual(mock_generate.call_count, 2)

    @patch('passwordGenerator.generateRandomLettersPassword')
    @patch('time.time', side_effect=[0, 5, 10, 15, 20, 25])
    def test_execute_for_letters_guesses_password(self, mock_time, mock_generate):
        # given
        mock_generate.side_effect = ['WrongPass', 'Password123']
        password = 'Password123'
        seconds = 30

        # when
        bruteForceRandomLength.executeForLetters(password, seconds)

        # then
        mock_generate.assert_called()
        self.assertEqual(mock_generate.call_count, 2)

    @patch('passwordGenerator.generateRandomAlphanumericPassword')
    @patch('time.time', side_effect=[0, 5, 10, 15, 20, 25])
    def test_execute_for_alphanumerics_guesses_password(self, mock_time, mock_generate):
        # given
        mock_generate.side_effect = ['wrongpass123', 'Password123']
        password = 'Password123'
        seconds = 30

        # when
        bruteForceRandomLength.executeForAlphanumerics(password, seconds)

        # then
        mock_generate.assert_called()
        self.assertEqual(mock_generate.call_count, 2)

    @patch('passwordGenerator.generateRandomAlphanumericPassword')
    @patch('time.time', side_effect=[0, 5, 10, 15, 20])
    def test_time_exceeded(self, mock_time, mock_generate):
        # given
        mock_generate.return_value = 'wrongpass123'
        password = 'Password123'
        seconds = 10

        # when
        bruteForceRandomLength.executeForAlphanumerics(password, seconds)

        # then
        mock_generate.assert_called()
        self.assertGreaterEqual(mock_generate.call_count, 1)


if __name__ == '__main__':
    unittest.main()
