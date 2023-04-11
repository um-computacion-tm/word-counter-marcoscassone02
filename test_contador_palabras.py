import unittest
from contador_palabras import contador_palabras
class TestContadorLetras(unittest.TestCase):
    def test_holamundo(self):
        resultado = contador_palabras("hola mundo")
        for i in resultado:
            self.assertEqual(resultado[i],1)
    def test_laverdad(self):
        resultado = contador_palabras("la verdad es que hay una mentira")
        for i in resultado:
            self.assertEqual(resultado[i],1)
    def test_pregunta(self):
        resultado = contador_palabras("no se que mas poner para saber si este test funciona, funciona o no?")
        for i in resultado:
            self.assertEqual(resultado[i],1)
    def test_definitivo1(self):
        resultado = contador_palabras("no no no no que no , que amigos")
        self.assertEqual(resultado["no"],5) 
    def test_definitivo2(self):
        resultado = contador_palabras("no no no no que no , que amigos")
        self.assertEqual(resultado["que"],2) 
    def test_definitivo3(self):
        resultado = contador_palabras("no no no no que no , que amigos")
        self.assertEqual(resultado["amigos"],1) 
    def test_definitivo3(self):
        resultado = contador_palabras("no no no no que no , que amigos")
        self.assertEqual(resultado[","],1) 
    def test_definitivo4(self):
        resultado = contador_palabras("un poco si, un poco no, se que un poco tambien")
        self.assertEqual(resultado["poco"],3) 
if __name__ == '__main__':
    unittest.main()
            
        
    
    