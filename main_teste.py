import unittest
from main import classificar_idade

class TestClassificarIdade(unittest.TestCase):

    def test_crianca(self):
        self.assertEqual(classificar_idade(0), "Criança")
        self.assertEqual(classificar_idade(5), "Criança")
        self.assertEqual(classificar_idade(12), "Criança")
    
    def test_adolescente(self):
        self.assertEqual(classificar_idade(13), "Adolescente")
        self.assertEqual(classificar_idade(15), "Adolescente")
        self.assertEqual(classificar_idade(17), "Adolescente")
    
    def test_adulto(self):
        self.assertEqual(classificar_idade(18), "Adulto")
        self.assertEqual(classificar_idade(30), "Adulto")
        self.assertEqual(classificar_idade(64), "Adulto")
    
    def test_idoso(self):
        self.assertEqual(classificar_idade(65), "Idoso")
        self.assertEqual(classificar_idade(80), "Idoso")
        self.assertEqual(classificar_idade(100), "Idoso")
    
    def test_idade_negativa(self):
        with self.assertRaises(ValueError):
            classificar_idade(-1)
    
    def test_idade_nao_inteira(self):
        with self.assertRaises(TypeError):
            classificar_idade("vinte")
        with self.assertRaises(TypeError):
            classificar_idade(25.5)

if __name__ == '__main__':
    unittest.main()

