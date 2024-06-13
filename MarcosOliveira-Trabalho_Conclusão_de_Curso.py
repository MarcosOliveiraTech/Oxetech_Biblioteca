from datetime import datetime

class Livro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._status = 'disponível'

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def status(self):
        return self._status

    def emprestar(self):
        if self._status == 'disponível':
            self._status = 'emprestado'
        else:
            print("Livro já está emprestado.")

    def devolver(self):
        if self._status == 'emprestado':
            self._status = 'disponível'
        else:
            print("Livro já está disponível.")

    def __str__(self):
        return f"Título: {self._titulo}, Autor: {self._autor}, Status: {self._status}"

class Membro:
    def __init__(self, nome, id_membro, endereco):
        self._nome = nome
        self._id_membro = id_membro
        self._endereco = endereco

    @property
    def nome(self):
        return self._nome

    @property
    def id_membro(self):
        return self._id_membro

    @property
    def endereco(self):
        return self._endereco

    def __str__(self):
        return f"Nome: {self._nome}, ID: {self._id_membro}, Endereço: {self._endereco}"

class Emprestimo:
    def __init__(self, livro, membro):
        self._livro = livro
        self._membro = membro
        self._data_emprestimo = datetime.now()
        self._data_devolucao = None
        self._estado = 'ativo'
        livro.emprestar()

    @property
    def livro(self):
        return self._livro

    @property
    def membro(self):
        return self._membro

    @property
    def data_emprestimo(self):
        return self._data_emprestimo

    @property
    def data_devolucao(self):
        return self._data_devolucao

    @property
    def estado(self):
        return self._estado

    def devolver(self):
        if self._estado == 'ativo':
            self._data_devolucao = datetime.now()
            self._estado = 'concluído'
            self._livro.devolver()
        else:
            print("Empréstimo já foi concluído.")

    def __str__(self):
        return f"Livro: {self._livro.titulo}, Membro: {self._membro.nome}, Data de Empréstimo: {self._data_emprestimo}, Estado: {self._estado}"

class Biblioteca:
    def __init__(self):
        self._livros = []  # Lista de livros
        self._membros = []  # Lista de membros
        self._emprestimos = []  # Lista de empréstimos
        self._clientes = []  # Matriz de clientes
        self._catalogo_livros = []  # Matriz de catálogo de livros

    def adicionar_livro(self, titulo):
        # Verifica se o livro já está no catálogo
        for livro in self._catalogo_livros:
            if livro[0] == titulo:
                livro[1] += 1  # Aumenta a quantidade do livro
                print(f"Quantidade de '{titulo}' atualizada para {livro[1]}.")
                return
        # Adiciona novo livro ao catálogo
        self._catalogo_livros.append([titulo, 1])
        print(f"Livro '{titulo}' adicionado ao catálogo.")

    def remover_livro(self, titulo):
        # Remove livro da lista de livros
        self._livros = [livro for livro in self._livros if livro.titulo != titulo]
        # Remove livro do catálogo
        self._catalogo_livros = [livro for livro in self._catalogo_livros if livro[0] != titulo]
        print(f"Livro '{titulo}' removido do catálogo.")

    def registrar_membro(self, nome, cpf, endereco):
        # Verifica se o cliente já está cadastrado
        for cliente in self._clientes:
            if cliente[1] == cpf and cliente[2] == 'Ativo':
                print("CPF já cadastrado e cliente está ativo.")
                return
        # Adiciona novo cliente à matriz de clientes
        self._clientes.append([nome, cpf, 'Ativo'])
        print("Cadastro concluído.")

    def remover_membro(self, cpf):
        # Marca cliente como 'Desativo' na matriz de clientes
        for cliente in self._clientes:
            if cliente[1] == cpf:
                cliente[2] = 'Desativo'
                print(f"Cliente com CPF {cpf} removido (marcado como 'Desativo').")
                return
        print("Cliente não encontrado.")

    def registrar_emprestimo(self, titulo_livro, id_membro):
        livro = next((livro for livro in self._livros if livro.titulo == titulo_livro and livro.status == 'disponível'), None)
        membro = next((membro for membro in self._membros if membro.id_membro == id_membro), None)
        if livro and membro:
            emprestimo = Emprestimo(livro, membro)
            self._emprestimos.append(emprestimo)
        else:
            print("Livro não disponível ou Membro não encontrado.")

    def registrar_devolucao(self, titulo_livro, id_membro):
        emprestimo = next((emp for emp in self._emprestimos if emp.livro.titulo == titulo_livro and emp.membro.id_membro == id_membro and emp.estado == 'ativo'), None)
        if emprestimo:
            emprestimo.devolver()
        else:
            print("Empréstimo não encontrado ou já concluído.")

    def listar_livros_disponiveis(self):
        return [livro for livro in self._livros if livro.status == 'disponível']

    def listar_livros_emprestados(self):
        return [livro for livro in self._livros if livro.status == 'emprestado']

    def locar_livro(self, titulo_livro):
        # Encontra o livro no catálogo
        for livro in self._catalogo_livros:
            if livro[0] == titulo_livro:
                if livro[1] < 1:
                    print("O livro encontra-se indisponível")
                else:
                    resposta = input(f"Deseja realmente locar '{titulo_livro}'? Ainda há {livro[1]} destes livros. Responda: S ou N: ")
                    if resposta.upper() == 'S':
                        livro[1] -= 1
                        print("Livro locado com sucesso.")
                    else:
                        print("Operação cancelada. Voltando para o menu principal.")
                return
        print("Livro não encontrado")

    def menu(self):
        while True:
            print("\nMenu Principal:")
            print("1 - Cadastrar Cliente")
            print("2 - Cadastrar Livro")
            print("3 - Locar Livro")
            print("4 - Remover Cliente")
            print("5 - Remover Livro")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome = input("Digite o nome do cliente: ")
                cpf = input("Digite o CPF do cliente: ")
                endereco = input("Digite o endereço do cliente: ")
                self.registrar_membro(nome, cpf, endereco)
            elif opcao == '2':
                titulo = input("Digite o título do livro: ")
                self.adicionar_livro(titulo)
            elif opcao == '3':
                titulo_livro = input("Digite o título do livro a ser locado: ")
                self.locar_livro(titulo_livro)
            elif opcao == '4':
                cpf = input("Digite o CPF do cliente a ser removido: ")
                self.remover_membro(cpf)
            elif opcao == '5':
                titulo = input("Digite o título do livro a ser removido: ")
                self.remover_livro(titulo)
            elif opcao == '0':
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Exemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.menu()
