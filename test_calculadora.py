import unittest
import tkinter as tk
from Calculadora_tkinter import entrar_valores, calcular, limpar_tela

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.todos_valores = ''
        self.valor_texto = tk.StringVar()

    def tearDown(self):
        self.root.destroy()

    def test_entrada_de_numeros(self):
        entrar_valores('1')
        self.assertEqual(self.todos_valores, '1')
        entrar_valores('2')
        self.assertEqual(self.todos_valores, '12')

    def test_limpar_tela(self):
        entrar_valores('123')
        limpar_tela()
        self.assertEqual(self.todos_valores, '')
        self.assertEqual(self.valor_texto.get(), '')

    def test_calculo_soma(self):
        entrar_valores('2+3')
        calcular()
        self.assertEqual(self.valor_texto.get(), '5')

    def test_calculo_subtracao(self):
        entrar_valores('5-3')
        calcular()
        self.assertEqual(self.valor_texto.get(), '2')

    def test_calculo_multiplicacao(self):
        entrar_valores('2*3')
        calcular()
        self.assertEqual(self.valor_texto.get(), '6')

    def test_calculo_divisao(self):
        entrar_valores('6/3')
        calcular()
        self.assertEqual(self.valor_texto.get(), '2.0')

if __name__ == '__main__':
    unittest.main()
