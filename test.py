import unittest 
import dojo

class listar(unittest.TestCase):
	def testa_lista_size(self):
		
		lista2 = dojo.umAcem()	
		self.assertEqual(
				range(1, 101),
				lista2
			)

	def testa_fizz(self):
		lista = range(1, 4)
		fizzTest = dojo.getElement(lista)

		self.assertEqual(
				"Fizz",
				dojo.getElement(lista)
			)
	def testa_buzz(self):
		lista = range(1, 6)
		self.assertEqual(
			"Buzz",
			dojo.getElement(lista)
			)


if __name__ == "__main__":
	unittest.main()

