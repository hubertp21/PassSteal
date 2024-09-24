import unittest
from unittest.mock import patch
import string

import passwordGenerator


class PasswordGeneratorTest(unittest.TestCase):

    @patch('random.randint', return_value=12)
    @patch('random.choice', side_effect=lambda x: x[0])
    def test_generate_default_random_password(self, mock_randint, mock_choice):
        # given when
        password = passwordGenerator.generateDefaultRandomPassword()

        # then
        self.assertEqual(password, string.ascii_letters[0] * 12)
        self.assertEqual(len(password), 12)

    @patch('random.randint', return_value=10)
    @patch('random.choice', side_effect=lambda x: x[0])
    def test_generate_random_lowercase_letters_password(self, mock_randint, mock_choice):
        # given when
        password = passwordGenerator.generateRandomLowercaseLettersPassword()

        # then
        self.assertEqual(password, string.ascii_lowercase[0] * 10)
        self.assertEqual(len(password), 10)

    @patch('random.randint', return_value=15)
    @patch('random.choice', side_effect=lambda x: x[0])
    def test_generate_random_uppercase_letters_password(self, mock_randint, mock_choice):
        # given when
        password = passwordGenerator.generateRandomUppercaseLettersPassword()

        # then
        self.assertEqual(password, string.ascii_uppercase[0] * 15)
        self.assertEqual(len(password), 15)

    @patch('random.randint', return_value=9)
    @patch('random.choice', side_effect=lambda x: x[0])
    def test_generate_random_letters_password(self, mock_randint, mock_choice):
        # given when
        password = passwordGenerator.generateRandomLettersPassword()

        # then
        self.assertEqual(password, string.ascii_letters[0] * 9)
        self.assertEqual(len(password), 9)

    @patch('random.randint', return_value=13)
    @patch('random.choice', side_effect=lambda x: x[0])
    def test_generate_random_alphanumeric_password(self, mock_randint, mock_choice):
        # given when
        password = passwordGenerator.generateRandomAlphanumericPassword()

        # then
        self.assertEqual(password, (string.ascii_letters + string.digits)[0] * 13)
        self.assertEqual(len(password), 13)

    @patch('random.choice', side_effect=lambda x: x[0])
    def test_generate_default_random_password_for_exact_length(self, mock_choice):
        # given when
        password = passwordGenerator.generateDefaultRandomPasswordForExactLength(10)

        # then
        self.assertEqual(password, (string.ascii_letters + string.digits + string.punctuation)[0] * 10)

    @patch('random.choice', side_effect=lambda x: x[0])
    def test_generate_random_lowercase_letters_password_for_exact_length(self, mock_choice):
        # given when
        password = passwordGenerator.generateRandomLowercaseLettersPasswordForExactLength(8)

        # then
        self.assertEqual(password, string.ascii_lowercase[0] * 8)

    @patch('random.choice', side_effect=lambda x: x[0])
    def test_generate_random_uppercase_letters_password_for_exact_length(self, mock_choice):
        # given when
        password = passwordGenerator.generateRandomUppercaseLettersPasswordForExactLength(14)

        # then
        self.assertEqual(password, string.ascii_uppercase[0] * 14)

    @patch('random.choice', side_effect=lambda x: x[0])
    def test_generate_random_letters_password_for_exact_length(self, mock_choice):
        # given when
        password = passwordGenerator.generateRandomLettersPasswordForExactLength(9)

        # then
        self.assertEqual(password, string.ascii_letters[0] * 9)

    @patch('random.choice', side_effect=lambda x: x[0])
    def test_generate_random_alphanumeric_password_for_exact_length(self, mock_choice):
        # given when
        password = passwordGenerator.generateRandomAlphanumericPasswordForExactLength(12)

        # then
        self.assertEqual(password, (string.ascii_letters + string.digits)[0] * 12)

    def test_generate_all_password_variations_for_dictionary_attack(self):
        # given when
        variations = passwordGenerator.generateAllPasswordVariationsForDictionaryAttack()
        expected_count = len(passwordGenerator.common_passwords) * len(passwordGenerator.password_variations)

        # then
        self.assertEqual(len(variations), expected_count)

    def test_generate_password_variations_with_exact_length_for_dictionary_attack(self):
        # given when
        variations = passwordGenerator.generatePasswordVariationsWithExactLengthForDictionaryAttack(11)

        # then
        for password in variations:
            self.assertEqual(len(password), 11)


if __name__ == "__main__":
    unittest.main()
