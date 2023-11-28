import unittest
import tkinter as tk
from Calculadora_tkinter import entrar_valores, calcular, limpar_tela, valor_texto, todos_valores

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.todos_valores = ''
        self.valor_texto = tk.StringVar()

    def tearDown(self):
        self.root.destroy()

    def test_entrada_de_numeros(self):
        entrar_valores('1')
        self.assertEqual(todos_valores, '1')
        entrar_valores('2')
        self.assertEqual(todos_valores, '12')

    def test_limpar_tela(self):
        entrar_valores('123')
        limpar_tela()
        self.assertEqual(todos_valores, '')
        self.assertEqual(valor_texto.get(), '')

class Test_Operacao_Adicao(unittest.TestCase):

    def test_soma(self):
        entrar_valores('2+3')
        calcular()
        self.assertEqual(valor_texto.get(), '5')

    def test_soma_negativa(self):
        entrar_valores('-2+3')
        calcular()
        self.assertNotEqual(valor_texto.get(), '5')

    def test_soma_igual(self):
        entrar_valores('2+3')
        entrar_valores('3+2')
        calcular()
        self.assertIs(valor_texto.get(), valor_texto.get())

class Test_Operacao_Subtracao(unittest.TestCase):

    def test_subtracao(self):
        entrar_valores('5-3')
        calcular()
        self.assertEqual(valor_texto.get(), '2')

    def test_subtracao_negativa(self):
        entrar_valores('-5-3')
        calcular()
        self.assertNotEqual(valor_texto.get(), '2')

    def test_subtracao_igual(self):
        entrar_valores('5-3')
        entrar_valores('5-3')
        calcular()
        self.assertIs(valor_texto.get(), valor_texto.get())

class Test_Operacao_Multiplicacao(unittest.TestCase):

    def test_multiplicacao(self):
        entrar_valores('2*3')
        calcular()
        self.assertEqual(valor_texto.get(), '6')

    def test_multiplicacao_negativa(self):
        entrar_valores('-2*3')
        calcular()
        self.assertNotEqual(valor_texto.get(), '6')

    def test_multiplicacao_igual(self):
        entrar_valores('2*3')
        calcular()
        resultado_esperado = 6.0  # Resultado esperado da multiplicação como um número de ponto flutuante
        self.assertEqual(float(valor_texto.get()), resultado_esperado)

class Test_Operacao_Divisao(unittest.TestCase):

    # No teste de divisão com decimais
    def test_divisao(self):
        entrar_valores('6/3')
        calcular()
        self.assertAlmostEqual(float(valor_texto.get()), 2.0, places=3)  # Comparar com precisão de 3 casas decimais

    def test_divisao_negativo(self):
        entrar_valores('-6/3')
        calcular()
        self.assertAlmostEqual(float(valor_texto.get()), -2.0, places=3)  # Comparar com precisão de 3 casas decimais

    def test_divisao_igual(self):
        entrar_valores('6/3')
        entrar_valores('6/3')
        calcular()
        resultado_esperado = '2.0'
        self.assertAlmostEqual(valor_texto.get(), resultado_esperado, places=3)  # Comparar com precisão de 3 casas decimais


if __name__ == '__main__':
    unittest.main()