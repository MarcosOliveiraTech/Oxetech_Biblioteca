# Definindo a classe Livro
class Livro:
    def __init__(self, titulo, autor, quantidade):
        self._titulo = titulo
        self._autor = autor
        self._quantidade = quantidade

    # Getters e Setters
    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, quantidade):
        self._quantidade = quantidade

    def incrementar_quantidade(self, quantidade=1):
        self._quantidade += quantidade

    def decrementar_quantidade(self, quantidade=1):
        self._quantidade -= quantidade

# Definindo a classe Membro
class Membro:
    def __init__(self, nome, cpf, status='Ativo'):
        self._nome = nome
        self._cpf = cpf
        self._status = status

    # Getters e Setters
    def get_nome(self):
        return self._nome

    def get_cpf(self):
        return self._cpf

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

# Definindo a classe Emprestimo
class Emprestimo:
    def __init__(self, livro, membro, data_emprestimo, data_devolucao=None):
        self._livro = livro
        self._membro = membro
        self._data_emprestimo = data_emprestimo
        self._data_devolucao = data_devolucao
        self._estado = 'ativo' if data_devolucao is None else 'concluido'

    # Getters e Setters
    def get_livro(self):
        return self._livro

    def get_membro(self):
        return self._membro

    def get_data_emprestimo(self):
        return self._data_emprestimo

    def get_data_devolucao(self):
        return self._data_devolucao

    def get_estado(self):
        return self._estado

    def set_data_devolucao(self, data_devolucao):
        self._data_devolucao = data_devolucao
        self._estado = 'concluido'

# Função principal para o menu inicial
def menu_inicial():
    print("Bem-vindo ao Sistema de Gestão de Biblioteca")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Livro")
    print("3 - Locar livro")
    print("4 - Remover cliente")
    print("5 - Remover livro")
    print("6 - Modo administrador")
    print("0 - Sair")

# Matrizes de clientes e livros
clientes = []
livros = []

# Função para cadastrar cliente
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    
    # Verificando se o CPF já está cadastrado e ativo
    for cliente in clientes:
        if cliente.get_cpf() == cpf and cliente.get_status() == 'Ativo':
            print("CPF já cadastrado e cliente está ativo")
            return
    
    # Adicionando novo cliente
    novo_cliente = Membro(nome, cpf)
    clientes.append(novo_cliente)
    print("Cadastro concluído")

# Função para cadastrar livro
def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    
    # Verificando se o livro já está cadastrado
    for livro in livros:
        if livro.get_titulo() == titulo:
            livro.incrementar_quantidade()
            print("Livro já cadastrado, quantidade incrementada")
            return
    
    # Adicionando novo livro
    autor = input("Digite o autor do livro: ")
    novo_livro = Livro(titulo, autor, quantidade=1)
    livros.append(novo_livro)
    print("Livro cadastrado com sucesso")

# Função para locar livro
def locar_livro():
    titulo = input("Digite o título do livro que deseja locar: ")
    
    # Buscando o livro
    for livro in livros:
        if livro.get_titulo() == titulo:
            if livro.get_quantidade() < 1:
                print("O livro encontra-se indisponível")
                return
            else:
                print(f"Deseja realmente locar {titulo}? Ainda há {livro.get_quantidade()} destes livros. Responda: S ou N")
                resposta = input().upper()
                if resposta == 'S':
                    livro.decrementar_quantidade()
                    print("Livro locado com sucesso")
                return
    
    print("Livro não encontrado")

# Função para remover cliente
def remover_cliente():
    cpf = input("Digite o CPF do cliente que deve ser excluído: ")
    
    # Verificando se o CPF está cadastrado
    for cliente in clientes:
        if cliente.get_cpf() == cpf:
            print(f"Deseja excluir {cliente.get_nome()} portador do cpf: {cpf}? S/N")
            resposta = input().upper()
            if resposta == 'S':
                clientes.remove(cliente)
                print("Cliente removido com sucesso")
            return
    
    print("CPF não encontrado")

# Função para remover livro
def remover_livro():
    titulo = input("Digite o nome do livro que deseja remover: ")
    
    # Verificando se o livro está cadastrado
    for livro in livros:
        if livro.get_titulo() == titulo:
            print(f"Deseja realmente excluir o livro {titulo} do seu acervo? S/N")
            resposta = input().upper()
            if resposta == 'S':
                livros.remove(livro)
                print("Livro removido com sucesso")
            return
    
    print("Livro não encontrado")

# Função do modo administrador
def modo_administrador():
    print("Modo Administrador")
    print("1 - Visualizar lista de clientes")
    print("2 - Visualizar lista de livros")
    print("3 - Histórico de locação")
    print("0 - Voltar ao menu principal")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        visualizar_lista_clientes()
    elif opcao == '2':
        visualizar_lista_livros()
    elif opcao == '3':
        historico_locacao()

# Função para visualizar lista de clientes
def visualizar_lista_clientes():
    print("Lista de Clientes:")
    for cliente in clientes:
        print(f"Nome: {cliente.get_nome()}, CPF: {cliente.get_cpf()}, Status: {cliente.get_status()}")

# Função para visualizar lista de livros
def visualizar_lista_livros():
    print("Lista de Livros:")
    for livro in livros:
        print(f"Título: {livro.get_titulo()}, Autor: {livro.get_autor()}, Quantidade: {livro.get_quantidade()}")

# Histórico de locações (para simplificar, vamos manter uma lista global)
historico_locacoes = []

# Função para registrar empréstimo
def registrar_emprestimo(livro, membro):
    import datetime
    data_emprestimo = datetime.date.today()
    novo_emprestimo = Emprestimo(livro, membro, data_emprestimo)
    historico_locacoes.append(novo_emprestimo)

# Função para visualizar histórico de locações
def historico_locacao():
    print("Histórico de Locações:")
    for emprestimo in historico_locacoes:
        print(f"Livro: {emprestimo.get_livro().get_titulo()}, Membro: {emprestimo.get_membro().get_nome()}, Data de Empréstimo: {emprestimo.get_data_emprestimo()}, Estado: {emprestimo.get_estado()}")

# Função principal
def main():
    while True:
        menu_inicial()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            cadastrar_livro()
        elif opcao == '3':
            locar_livro()
        elif opcao == '4':
            remover_cliente()
        elif opcao == '5':
            remover_livro()
        elif opcao == '6':
            modo_administrador()
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
