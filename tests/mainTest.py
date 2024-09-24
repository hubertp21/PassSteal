import unittest
from unittest.mock import patch
import sys

import main


class MainTest(unittest.TestCase):

    @patch('bruteForce.bruteForceExecutor.executeBruteForceAlgorithm')
    @patch('dictionaryAttack.dictionaryAttackExecutor.executeDictionaryAttackAlgorithm')
    def test_bruteforce_algorithm_execution(self, mock_dict_attack, mock_brute_force):
        # given
        sys.argv = ['script_name', 'password123', '20', 'bruteForce']

        # when
        main.main()

        # then
        mock_brute_force.assert_called_with('password123', 20)
        mock_dict_attack.assert_not_called()

    @patch('dictionaryAttack.dictionaryAttackExecutor.executeDictionaryAttackAlgorithm')
    @patch('bruteForce.bruteForceExecutor.executeBruteForceAlgorithm')
    def test_dictionary_attack_algorithm_execution(self, mock_brute_force, mock_dict_attack):
        # given
        sys.argv = ['script_name', 'password123', '20', 'dictionaryAttack']

        # when
        main.main()

        # then
        mock_dict_attack.assert_called_with('password123', 20)
        mock_brute_force.assert_not_called()

    def test_short_password_error(self):
        # given
        sys.argv = ['script_name', '1234', '20', 'bruteForce']

        # when then
        with self.assertRaises(SystemExit):
            main.main()

    def test_time_too_short_error(self):
        # given
        sys.argv = ['script_name', 'password123', 5, 'bruteForce']

        # when then
        with self.assertRaises(SystemExit):
            main.main()

    def test_invalid_algorithm_error(self):
        # given
        sys.argv = ['script_name', 'password123', '20', 'unknownAlgorithm']

        # when then
        with self.assertRaises(SystemExit):
            main.main()


if __name__ == '__main__':
    unittest.main()
