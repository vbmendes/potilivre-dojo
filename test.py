import unittest 
import dojo

class listar(unittest.TestCase):
	def testa_lista_size(self):
		lista2 = dojo.umAcem()	
		self.assertEqual(
				100,
				len(lista2)
			)

	def testa_fizz(self):
		fizzTest = dojo.fizzbuzz(3)
		self.assertEqual(
				"Fizz",
				fizzTest
			)
	def testa_buzz(self):
		fizzTest = dojo.fizzbuzz(5)
		self.assertEqual(
			"Buzz",
			fizzTest
			)
	
	def testa_fizzbuzz(self):
		fizzTest = dojo.fizzbuzz(15)
		self.assertEqual(
			"FizzBuzz",
			fizzTest
			)


if __name__ == "__main__":
	unittest.main()

