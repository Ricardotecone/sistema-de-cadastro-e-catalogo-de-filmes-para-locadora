>> Sistema de Cadastro de Filmes para Locadora
>> Classes, Atributos e Funções


# Filme #
Esta classe representa um filme disponível para locação na locadora.
* id_filme (Int): Identificador único do filme.
* titulo (String): Título do filme.
* diretor (String): Nome do diretor do filme.
* ano_lancamento (Int): Ano de lançamento do filme.
* duracao (Int): Duração em minutos.
* quantidade_estoque (Int): Quantidade de cópias disponíveis.
* quantidade_total (Int): Quantidade total de cópias.
* genero_id (Int): Chave estrangeira para o gênero do filme.
Suas funções (Métodos):
* verificar_disponibilidade(): Retorna True se houver cópias disponíveis.
* adicionar_estoque(quantidade): Adiciona cópias ao estoque.
* remover_estoque(quantidade): Remove cópias do estoque.
* obter_atores(): Retorna lista de atores do filme.


# Ator #
Esta classe representa um ator que pode participar de um ou mais filmes.
* id_ator (Int): Identificador único do ator.
* nome (String): Nome completo do ator.
* data_nascimento (Date): Data de nascimento do ator.
* nacionalidade (String): Nacionalidade do ator.
Suas funções (Métodos):
* obter_filmes(): Retorna lista de filmes em que o ator participou.
* adicionar_filme(filme): Adiciona um filme à filmografia do ator.


# Genero #
Esta classe representa o gênero cinematográfico de um filme.
* id_genero (Int): Identificador único do gênero.
* nome (String): Nome do gênero (ex: Ação, Comédia, Drama).
* descricao (String): Descrição do gênero.


# FilmeAtor (Classe de Associação) #
Esta classe resolve a relação muitos-para-muitos entre Filme e Ator.
* id_filme_ator (Int): Identificador único da relação.
* id_filme (Int): Chave estrangeira para Filme.id_filme.
* id_ator (Int): Chave estrangeira para Ator.id_ator.
* personagem (String): Nome do personagem interpretado pelo ator.


# Relações e Conexões (Multiplicidade) #
Genero 1 para * Filme → Um gênero pode ter vários filmes.
Filme * para * Ator → Um filme pode ter vários atores e um ator pode participar de vários filmes (resolvido pela classe FilmeAtor).