from datetime import date
from typing import List


class Ator:
    def __init__(self, id_ator: int, nome: str, data_nascimento: date, nacionalidade: str):
        self.__id_ator = id_ator
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__nacionalidade = nacionalidade
        self.__atuacoes: List[Atuacao] = []

    def adicionar_atuacao(self, atuacao: 'Atuacao'):
        self.__atuacoes.append(atuacao)

    def obter_atuacao(self) -> List['Atuacao']:
        return self.__atuacoes

    def __str__(self):
        return f"{self.__nome} ({self.__nacionalidade})"


class Filme:
    def __init__(self, id_filme: int, titulo: str, diretor: str, ano_lancamento: int, 
                 duracao: int, quantidade_total: int, genero: str):
        self.__id_filme = id_filme
        self.__titulo = titulo
        self.__diretor = diretor
        self.__ano_lancamento = ano_lancamento
        self.__duracao = duracao
        self.__quantidade_total = quantidade_total
        self.__genero = genero
        self.__atuacoes: List[Atuacao] = []

    def verificar_disponiveis(self) -> bool:
        return self.__quantidade_total > 0

    def adicionar_estoque(self, quantidade: int):
        if quantidade > 0:
            self.__quantidade_total += quantidade

    def remover_estoque(self, quantidade: int):
        if 0 < quantidade <= self.__quantidade_total:
            self.__quantidade_total -= quantidade

    def adicionar_atuacao(self, atuacao: 'Atuacao'):
        self.__atuacoes.append(atuacao)

    def obter_atuacao(self) -> List['Atuacao']:
        return self.__atuacoes

    def __str__(self):
        return f"{self.__titulo} ({self.__ano_lancamento})"


class Atuacao:
    def __init__(self, id_filme_ator: int, filme: Filme, ator: Ator, personagem: str):
        self.__id_filme_ator = id_filme_ator
        self.__filme = filme
        self.__ator = ator
        self.__personagem = personagem

        # Associação bidirecional
        filme.adicionar_atuacao(self)
        ator.adicionar_atuacao(self)

    def adicionarAtuacao(self, ator: Ator):
        self.__ator = ator

    def __str__(self):
        return f"{self.__ator} como {self.__personagem} em '{self.__filme}'"


# ==== Exemplo de uso (teste básico) ====
if __name__ == "__main__":
    filme1 = Filme(1, "Matrix", "Wachowski", 1999, 136, 10, "Ficção Científica")
    ator1 = Ator(1, "Keanu Reeves", date(1964, 9, 2), "Canadense")

    atuacao1 = Atuacao(1, filme1, ator1, "Neo")

    print(filme1)
    print("Atores no filme:")
    for atuacao in filme1.obter_atuacao():
        print("-", atuacao)

    print("\nVerificando disponibilidade:", filme1.verificar_disponiveis())
    filme1.remover_estoque(2)
    print("Estoque atualizado:", filme1.verificar_disponiveis())
