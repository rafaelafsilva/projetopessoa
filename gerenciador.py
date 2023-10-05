from pessoa import Pessoa

class GerenciadorPessoas:
    def __init__(self):
        self.pessoas = []

    def cadastrar_pessoa(self, nome, data_nascimento, endereco, cpf, estado_civil):
        pessoa = Pessoa(nome, data_nascimento, endereco, cpf, estado_civil)
        self.pessoas.append(pessoa)

    def listar_pessoas(self):
        return self.pessoas

    def buscarPessoa(self, cpf):
        for pessoa in self.pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        return None

    def atualizar_pessoa(self, cpf, nome, data_nascimento, endereco, estado_civil):
        pessoa = self.buscarPessoa(cpf)
        if pessoa:
            pessoa.nome = nome
            pessoa.data_nascimento = data_nascimento
            pessoa.endereco = endereco
            pessoa.estado_civil = estado_civil
            return True
        else:
            return False

    def excluir_pessoa(self, cpf):
        pessoa = self.buscarPessoa(cpf)
        if pessoa:
            self.pessoas.remove(pessoa)
            return True
        else:
            return False
