# -*- coding: utf-8 -*-

from unittest import TestCase
from app.filme import Filme
from app.filme import NotaForaDoIntervaloDefinidoException, NomeDoFilmeVazioException

class TestFilme(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.filme = Filme('Matrix', 6)

    def test_mostraNome(self):
        self.assertEqual(self.filme.mostraNome(), 'Matrix');

    def test_mostraNota(self):
        self.assertEqual(self.filme.mostraNota(), 6)

    def test_nomeVazio(self):
        metodo = self.filme.verificaNomeVazio
        self.assertRaises(NomeDoFilmeVazioException, metodo, '')
        self.assertRaises(NomeDoFilmeVazioException, metodo, None)
        self.assertRaises(NomeDoFilmeVazioException, metodo, False)
        self.assertRaises(NomeDoFilmeVazioException, metodo, 0)

    def test_intervaloNotaNegativa(self):
        metodo = self.filme.verificaIntervaloDaNota
        self.assertRaises(NotaForaDoIntervaloDefinidoException, metodo, -1)

    def test_intervaloNotaAcimaDoLimite(self):
        metodo = self.filme.verificaIntervaloDaNota
        self.assertRaises(NotaForaDoIntervaloDefinidoException, metodo, 7)

    def test_valorDaNotaNaoNumerico(self):
        metodo = self.filme.verificaNumeroNota
        self.assertRaises(ValueError, metodo, 'String')
