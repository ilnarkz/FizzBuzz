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
        assert out[0] == 'Buzz!'
        assert out[1] == '11'
        assert out[2] == 'Fizz!'
        assert out[3] == 'FizzBuzz!'
        assert out[4] == 'Please, input the number!'
        assert out[5] == 'Please, input the number!'
        assert out[6] == 'Please, input the number!'

