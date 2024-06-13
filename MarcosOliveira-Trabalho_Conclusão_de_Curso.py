
from datetime import datetime

# Classe Livro: Representa um livro com título, autor e status.
class Livro:
    def __init__(self, titulo, autor):
        self._titulo = titulo  # Atributo privado para armazenar o título do livro
        self._autor = autor    # Atributo privado para armazenar o autor do livro
        self._status = 'disponível'  # Atributo privado para armazenar o status do livro

    # Getter para o título do livro
    @property
    def titulo(self):
        return self._titulo

    # Getter para o autor do livro
    @property
    def autor(self):
        return self._autor

    # Getter para o status do livro
    @property
    def status(self):
        return self._status

    # Método para emprestar o livro (muda o status para 'emprestado')
    def emprestar(self):
        if self._status == 'disponível':
            self._status = 'emprestado'
        else:
            print("Livro já está emprestado.")

    # Método para devolver o livro (muda o status para 'disponível')
    def devolver(self):
        if self._status == 'emprestado':
            self._status = 'disponível'
        else:
            print("Livro já está disponível.")

    # Método para representar o livro como string (para fácil visualização)
    def __str__(self):
        return f"Título: {self._titulo}, Autor: {self._autor}, Status: {self._status}"

# Classe Membro: Representa um membro da biblioteca com nome, ID e endereço.
class Membro:
    def __init__(self, nome, id_membro, endereco):
        self._nome = nome  # Atributo privado para armazenar o nome do membro
        self._id_membro = id_membro  # Atributo privado para armazenar o ID do membro
        self._endereco = endereco  # Atributo privado para armazenar o endereço do membro

    # Getter para o nome do membro
    @property
    def nome(self):
        return self._nome

    # Getter para o ID do membro
    @property
    def id_membro(self):
        return self._id_membro

    # Getter para o endereço do membro
    @property
    def endereco(self):
        return self._endereco

    # Método para representar o membro como string (para fácil visualização)
    def __str__(self):
        return f"Nome: {self._nome}, ID: {self._id_membro}, Endereço: {self._endereco}"

# Classe Emprestimo: Gerencia o empréstimo de livros, com data de empréstimo, devolução e estado.
class Emprestimo:
    def __init__(self, livro, membro):
        self._livro = livro  # Atributo privado para armazenar o livro emprestado
        self._membro = membro  # Atributo privado para armazenar o membro que fez o empréstimo
        self._data_emprestimo = datetime.now()  # Data e hora do empréstimo
        self._data_devolucao = None  # Data de devolução (inicialmente None)
        self._estado = 'ativo'  # Estado do empréstimo (ativo ou concluído)
        livro.emprestar()  # Muda o status do livro para 'emprestado'

    # Getter para o livro emprestado
    @property
    def livro(self):
        return self._livro

    # Getter para o membro que fez o empréstimo
    @property
    def membro(self):
        return self._membro

    # Getter para a data de empréstimo
    @property
    def data_emprestimo(self):
        return self._data_emprestimo

    # Getter para a data de devolução
    @property
    def data_devolucao(self):
        return self._data_devolucao

    # Getter para o estado do empréstimo
    @property
    def estado(self):
        return self._estado

    # Método para devolver o livro (muda o estado do empréstimo e o status do livro)
    def devolver(self):
        if self._estado == 'ativo':
            self._data_devolucao = datetime.now()
            self._estado = 'concluído'
            self._livro.devolver()
        else:
            print("Empréstimo já foi concluído.")

    # Método para representar o empréstimo como string (para fácil visualização)
    def __str__(self):
        return f"Livro: {self._livro.titulo}, Membro: {self._membro.nome}, Data de Empréstimo: {self._data_emprestimo}, Estado: {self._estado}"

# Classe Biblioteca: Gerencia os livros, membros e empréstimos da biblioteca.
class Biblioteca:
    def __init__(self):
        self._livros = []  # Lista para armazenar os livros
        self._membros = []  # Lista para armazenar os membros
        self._emprestimos = []  # Lista para armazenar os empréstimos

    # Método para adicionar um livro à biblioteca
    def adicionar_livro(self, livro):
        self._livros.append(livro)

    # Método para remover um livro da biblioteca pelo título
    def remover_livro(self, titulo):
        self._livros = [livro for livro in self._livros if livro.titulo != titulo]

    # Método para atualizar os detalhes de um livro
    def atualizar_livro(self, titulo, novo_titulo, novo_autor):
        for livro in self._livros:
            if livro.titulo == titulo:
                livro._titulo = novo_titulo
                livro._autor = novo_autor

    # Método para registrar um novo membro na biblioteca
    def registrar_membro(self, membro):
        self._membros.append(membro)

    # Método para registrar um empréstimo de livro
    def registrar_emprestimo(self, titulo_livro, id_membro):
        # Encontra o livro disponível pelo título
        livro = next((livro for livro in self._livros if livro.titulo == titulo_livro and livro.status == 'disponível'), None)
        # Encontra o membro pelo ID
        membro = next((membro for membro in self._membros if membro.id_membro == id_membro), None)
        if livro and membro:
            emprestimo = Emprestimo(livro, membro)
            self._emprestimos.append(emprestimo)
        else:
            print("Livro não disponível ou Membro não encontrado.")

    # Método para registrar a devolução de um livro
    def registrar_devolucao(self, titulo_livro, id_membro):
        # Encontra o empréstimo ativo pelo título do livro e ID do membro
        emprestimo = next((emp for emp in self._emprestimos if emp.livro.titulo == titulo_livro and emp.membro.id_membro == id_membro and emp.estado == 'ativo'), None)
        if emprestimo:
            emprestimo.devolver()
        else:
            print("Empréstimo não encontrado ou já concluído.")

    # Método para listar os livros disponíveis na biblioteca
    def listar_livros_disponiveis(self):
        return [livro for livro in self._livros if livro.status == 'disponível']

    # Método para listar os livros emprestados na biblioteca
    def listar_livros_emprestados(self):
        return [livro for livro in self._livros if livro.status == 'emprestado']

# Exemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Adicionar livros à biblioteca
    livro1 = Livro("Python Programming", "John Doe")
    livro2 = Livro("Machine Learning", "Jane Doe")
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    # Registrar membros na biblioteca
    membro1 = Membro("Alice", 1, "Rua A, 123")
    membro2 = Membro("Bob", 2, "Rua B, 456")
    biblioteca.registrar_membro(membro1)
    biblioteca.registrar_membro(membro2)

    # Registrar empréstimo de um livro
    biblioteca.registrar_emprestimo("Python Programming", 1)

    # Listar livros disponíveis e emprestados
    print("Livros disponíveis:")
    for livro in biblioteca.listar_livros_disponiveis():
        print(livro)

    print("\nLivros emprestados:")
    for livro in biblioteca.listar_livros_emprestados():
        print(livro)

    # Registrar devolução de um livro
    biblioteca.registrar_devolucao("Python Programming", 1)

    print("\nLivros disponíveis após devolução:")
    for livro in biblioteca.listar_livros_disponiveis():
        print(livro)
