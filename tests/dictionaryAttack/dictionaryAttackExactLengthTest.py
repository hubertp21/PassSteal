import unittest
from unittest.mock import patch
import time

from dictionaryAttack import dictionaryAttackExactLength


class DictionaryAttackExactLengthTest(unittest.TestCase):

    @patch('passwordGenerator.generatePasswordVariationsWithExactLengthForDictionaryAttack')
    def test_execute_for_exact_length_success(self, mock_generate_passwords):
        # given
        password = 'password123'
        seconds = 5
        mock_generate_passwords.return_value = ['wrongpass', 'password123', 'anotherwrongpass']

        # when
        with patch('time.time', side_effect=[time.time(), time.time() + 1]):
            dictionaryAttackExactLength.executeForExactLength(password, seconds)

        # then
        self.assertIn('password123', mock_generate_passwords.return_value)

    @patch('passwordGenerator.generatePasswordVariationsWithExactLengthForDictionaryAttack')
    def test_execute_for_exact_length_failure(self, mock_generate_passwords):
        # given
        password = 'password123'
        seconds = 2
        mock_generate_passwords.return_value = ['wrongpass', 'anotherwrongpass']

        # when
        start_time = time.time()
        dictionaryAttackExactLength.executeForExactLength(password, seconds)
        elapsed_time = time.time() - start_time

        # then
        self.assertGreater(elapsed_time, 2)
        self.assertEqual(mock_generate_passwords.call_count, 1)


if __name__ == '__main__':
    unittest.main()
