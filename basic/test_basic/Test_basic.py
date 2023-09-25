from unittest import TestCase

from basic_client import cliente
from basic_server import servidor
class Test_Client(TestCase):
    def test_cliente(self):
        self.assertEqual(cliente(),True)
class Test_Server(TestCase):
    def test_server(self):
        self.assertEqual(servidor(),True)