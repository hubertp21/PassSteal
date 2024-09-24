import unittest
from unittest.mock import patch

from dictionaryAttack import dictionaryAttackExecutor


class DictionaryAttackExecutorTest(unittest.TestCase):

    @patch('builtins.input', return_value='y')
    @patch('dictionaryAttack.dictionaryAttackExecutor.executeDictionaryAttackForPasswordLength')
    def test_execute_dictionary_attack_algorithm_exact_length_enabled(self, mock_execute_exact_length, mock_input):
        # given
        password = 'password123'
        seconds = 30

        # when
        dictionaryAttackExecutor.executeDictionaryAttackAlgorithm(password, seconds)

        # then
        mock_input.assert_called_once_with("Do you want to enable exact length guessing? (y/n) ")
        mock_execute_exact_length.assert_called_once_with(password, seconds)

    @patch('builtins.input', return_value='n')
    @patch('dictionaryAttack.dictionaryAttackExecutor.executeDictionaryAttack')
    def test_execute_dictionary_attack_algorithm_exact_length_disabled(self, mock_execute_random_length, mock_input):
        # given
        password = 'password123'
        seconds = 30

        # when
        dictionaryAttackExecutor.executeDictionaryAttackAlgorithm(password, seconds)

        # then
        mock_input.assert_called_once_with("Do you want to enable exact length guessing? (y/n) ")
        mock_execute_random_length.assert_called_once_with(password, seconds)

    @patch('dictionaryAttack.dictionaryAttackExactLength.executeForExactLength')
    @patch('builtins.input', side_effect=['y'])
    def test_execute_dictionary_attack_for_password_length(self, mock_input, mock_execute_exact_length):
        # given
        password = 'password123'
        seconds = 30

        # when
        dictionaryAttackExecutor.executeDictionaryAttackForPasswordLength(password, seconds)

        # then
        mock_execute_exact_length.assert_called_once_with(password, seconds)

    @patch('dictionaryAttack.dictionaryAttackRandomLength.executeForRandomLength')
    @patch('builtins.input', side_effect=['n'])
    def test_execute_dictionary_attack(self, mock_input, mock_execute_random_length):
        # given
        password = 'password123'
        seconds = 30

        # when
        dictionaryAttackExecutor.executeDictionaryAttack(password, seconds)

        # then
        mock_execute_random_length.assert_called_once_with(password, seconds)


if __name__ == '__main__':
    unittest.main()
