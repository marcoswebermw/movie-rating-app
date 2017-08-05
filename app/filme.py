# _*_ coding: utf-8 _*_

class Filme(object):

    def __init__(self, nome, nota=0, observacao='Nenhuma observação.'):
        self.verificaNomeVazio(nome)
        self.verificaNumeroNota(nota)
        self.observacao = observacao

    def mostraNome(self):
        return self.nome

    def mostraNota(self):
        return self.nota

    def mostraObservacao(self):
        return self.observacao

    def verificaNomeVazio(self, nome):
        if not nome:
            raise NomeDoFilmeVazioException
        else:
            self.nome = nome

    def verificaNumeroNota(self, nota):
        if isinstance(nota, int):
            self.verificaIntervaloDaNota(nota)
        else:
            raise ValueError

    def verificaIntervaloDaNota(self, nota):
        if nota >= 0 and nota <=6:
            self.nota = nota
        else:
            raise NotaForaDoIntervaloDefinidoException(nota)



class NomeDoFilmeVazioException(Exception):

    def __str__(self):
        return "O nome do filme não pode ficar vazio."


class NotaForaDoIntervaloDefinidoException(Exception):

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "A nota {} está fora do intervalo definido.".format(self.valor)
