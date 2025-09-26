from typing import List, Optional
from datetime import date

class Genero:
    def __init__(self, id_genero: int, nome: str, descricao: str = ""):
        self.id_genero = id_genero
        self.nome = nome
        self.descricao = descricao

class Ator:
    def __init__(self, id_ator: int, nome: str, data_nascimento: date, nacionalidade: str):
        self.id_ator = id_ator
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.nacionalidade = nacionalidade
        self.filmes: List[Filme] = []
    
    def obter_filmes(self) -> List['Filme']:
        print(self.filmes)
        return self.filmes
    
    def adicionar_filme(self, filme: 'Filme'):
        if filme not in self.filmes:
            self.filmes.append(filme)

class Filme:
    def __init__(self, id_filme: int, titulo: str, diretor: str, ano_lancamento: int, 
                 duracao: int, genero: Genero, quantidade_total: int = 1):
        self.id_filme = id_filme
        self.titulo = titulo
        self.diretor = diretor
        self.ano_lancamento = ano_lancamento
        self.duracao = duracao
        self.genero = genero
        self.quantidade_total = quantidade_total
        self.quantidade_estoque = quantidade_total
        self.atores: List[Ator] = []
    
    def verificar_disponibilidade(self) -> bool:
        return self.quantidade_estoque > 0
    
    def adicionar_estoque(self, quantidade: int):
        self.quantidade_estoque += quantidade
        self.quantidade_total += quantidade
    
    def remover_estoque(self, quantidade: int):
        if self.quantidade_estoque >= quantidade:
            self.quantidade_estoque -= quantidade
    
    def obter_atores(self) -> List[Ator]:
        return self.atores
    
    def adicionar_ator(self, ator: Ator, personagem: str = ""):
        if ator not in self.atores:
            self.atores.append(ator)
            ator.adicionar_filme(self)

class Locadora:
    def __init__(self):
        self.filmes: List[Filme] = []
        self.atores: List[Ator] = []
        self.generos: List[Genero] = []
    
    def adicionar_filme(self, filme: Filme):
        self.filmes.append(filme)
    
    def buscar_por_genero(self, genero_nome: str) -> List[Filme]:
        return [filme for filme in self.filmes if filme.genero.nome.lower() == genero_nome.lower()]
    
    def buscar_filmes_disponiveis(self) -> List[Filme]:
        return [filme for filme in self.filmes if filme.verificar_disponibilidade()]



# --- Exemplo de uso das classes ---
if __name__ == "__main__":
    # 1. Criar alguns gêneros
    genero_acao = Genero(id_genero=1, nome="Ação", descricao="Filmes com muita adrenalina.")
    genero_comedia = Genero(id_genero=2, nome="Comédia", descricao="Filmes para rir.")
    
    # 2. Criar alguns atores
    ator_chris = Ator(id_ator=101, nome="Chris Evans", data_nascimento=date(1981, 6, 13), nacionalidade="Americana")
    ator_ryan = Ator(id_ator=102, nome="Ryan Reynolds", data_nascimento=date(1976, 10, 23), nacionalidade="Canadense")

    # 3. Criar a locadora
    minha_locadora = Locadora()
    
    # 4. Criar alguns filmes e adicioná-los à locadora
    filme1 = Filme(id_filme=1001, titulo="Vingadores", diretor="Irmãos Russo", ano_lancamento=2012, 
                   duracao=143, genero=genero_acao, quantidade_total=3)
    filme2 = Filme(id_filme=1002, titulo="Deadpool", diretor="Tim Miller", ano_lancamento=2016, 
                   duracao=108, genero=genero_comedia, quantidade_total=2)

    minha_locadora.adicionar_filme(filme1)
    minha_locadora.adicionar_filme(filme2)

    # 5. Adicionar atores aos filmes
    filme1.adicionar_ator(ator_chris)
    filme2.adicionar_ator(ator_ryan)

    # 6. Testar as funcionalidades
    print("--- Filmes Disponíveis ---")
    filmes_disponiveis = minha_locadora.buscar_filmes_disponiveis()
    for f in filmes_disponiveis:
        print(f"Título: {f.titulo}, Gênero: {f.genero.nome}, Em Estoque: {f.quantidade_estoque}")
    
    print("\n--- Buscando por Gênero: Ação ---")
    filmes_de_acao = minha_locadora.buscar_por_genero("Ação")
    for f in filmes_de_acao:
        print(f"Filme de Ação encontrado: {f.titulo}")

    print(f"\nDisponibilidade de '{filme1.titulo}': {filme1.verificar_disponibilidade()}")

    # 7. Simular a locação (removendo estoque)
    print(f"\nLocando uma cópia de '{filme1.titulo}'...")
    filme1.remover_estoque(1)
    print(f"Nova quantidade em estoque de '{filme1.titulo}': {filme1.quantidade_estoque}")