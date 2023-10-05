from gerenciador import GerenciadorPessoas

class Main:
    def __init__(self):
        self.gerenciador = GerenciadorPessoas()

    def mostrar_menu(self):
        while True:
            print("\nMenu de Opções:")
            print("1. Cadastrar Pessoa")
            print("2. Listar Pessoas")
            print("3. Atualizar Pessoa")
            print("4. Excluir Pessoa")
            print("5. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.cadastrar_pessoa()
            elif escolha == "2":
                self.listar_pessoas()
            elif escolha == "3":
                self.atualizar_pessoa()
            elif escolha == "4":
                self.excluir_pessoa()
            elif escolha == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def cadastrar_pessoa(self):
        nome = input("Digite o Nome Completo: ")
        data_nascimento = input("Digite a Data de Nascimento (YYYY-MM-DD): ")
        endereco = input("Digite o Endereço: ")
        cpf = input("Digite o CPF: ")
        estado_civil = input("Digite o Estado Civil: ")

        self.gerenciador.cadastrar_pessoa(nome, data_nascimento, endereco, cpf, estado_civil)
        print("Pessoa cadastrada com sucesso!")

    def listar_pessoas(self):
        pessoas = self.gerenciador.listar_pessoas()
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
        else:
            print("Pessoas cadastradas:")
            for pessoa in pessoas:
                print(f"Nome: {pessoa.nome}, CPF: {pessoa.cpf}")

    def atualizar_pessoa(self):
        cpf = input("Digite o CPF da pessoa que deseja atualizar: ")
        pessoa = self.gerenciador.buscarPessoa(cpf)
        if pessoa:
            nome = input("Novo Nome: ")
            data_nascimento = input("Nova Data de Nascimento (YYYY-MM-DD): ")
            endereco = input("Novo Endereço: ")
            estado_civil = input("Novo Estado Civil: ")

            if self.gerenciador.atualizar_pessoa(cpf, nome, data_nascimento, endereco, estado_civil):
                print("Pessoa atualizada com sucesso!")
            else:
                print(f"Pessoa com CPF {cpf} não encontrada.")
        else:
            print(f"Pessoa com CPF {cpf} não encontrada.")

    def excluir_pessoa(self):
        cpf = input("Digite o CPF da pessoa que deseja excluir: ")
        if self.gerenciador.excluir_pessoa(cpf):
            print("Pessoa excluída com sucesso!")
        else:
            print(f"Pessoa com CPF {cpf} não encontrada.")

if __name__ == "__main__":
    app = Main()
    app.mostrar_menu()
