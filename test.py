import unittest

from hello import hello

class Testes(unittest.TestCase):
	def test_func(self):
		self.assertEqual(hello(), "Teste da APia")

if __name__ == '__main__':
	unittest.main()
