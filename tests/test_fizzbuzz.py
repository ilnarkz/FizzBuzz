import sys
import threading

from unittest import TestCase
from unittest.mock import patch

import pytest

from fizz_buzz.scripts.fizz_buzz import run


def test_fizzbuzz(capsys):
    with patch("builtins.input") as input_mock:
        input_mock.side_effect = ['10', '11', '12', '15', 'W', '/', '', 'q']
        run()
        out, err = capsys.readouterr()
        sys.stdout.write(out)
        out = out.split('\n')
        assert 'Welcome to Fizz Buzz!' in out
        assert 'Submit a number and get an answer!' in out
        assert 'If you want to exit, press "q".' in out
        assert out[3] == 'Buzz!'
        assert out[4] == '11'
        assert out[5] == 'Fizz!'
        assert out[6] == 'FizzBuzz!'
        assert out[7] == 'Please, input the number!'
        assert out[8] == 'Please, input the number!'
        assert out[9] == 'Please, input the number!'

