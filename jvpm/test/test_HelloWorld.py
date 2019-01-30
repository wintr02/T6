#Team Members: Steven Wancewicz
#              Christian Waldron
#              Claire Wiesner

import unittest
import sys
import jvpm.HelloWorld
from unittest.mock import Mock, call

class TestHelloWorld(unittest.TestCase):
    def test_HelloWorld(self):
        sys.stdout = unittest.mock.Mock()
        jvpm.HelloWorld.HelloWorld()
        sys.stdout.assert_has_calls(
            [call.write('Hello world'), call.write('\n'), call.write('Hello Steven Wancewicz'), call.write('\n'),
			call.write('Hello Christian Waldron'), call.write('\n'), call.write('Hello Claire Wiesner'),
                        call.write('\n')])
