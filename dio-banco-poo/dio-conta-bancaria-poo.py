# Desafio DIO - Conta bancária com POO - Rafael Inocente Pavão

from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if conta in self.contas:
            transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self._quantidade_saques = 0

    def sacar(self, valor):
        if valor > self.limite:
            print("Saque excede o limite permitido.")
            return False

        if self._quantidade_saques >= self.limite_saques:
            print("Limite de saques diários atingido.")
            return False

        if super().sacar(valor):
            self._quantidade_saques += 1
            return True

        print("Saldo insuficiente.")
        return False


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar_transacao(self)


def main():
    cliente_joao = PessoaFisica(nome="João", data_nascimento="01/01/1980", cpf="12345678900", endereco="Rua 1")
    conta_joao = ContaCorrente.nova_conta(cliente_joao, numero=1)
    cliente_joao.adicionar_conta(conta_joao)

    cliente_maria = PessoaFisica(nome="Maria", data_nascimento="02/02/1990", cpf="09876543211", endereco="Rua 2")
    conta_maria = ContaCorrente.nova_conta(cliente_maria, numero=2)
    cliente_maria.adicionar_conta(conta_maria)

    # Transações
    deposito_joao = Deposito(1000)
    cliente_joao.realizar_transacao(conta_joao, deposito_joao)

    saque_joao = Saque(300)
    cliente_joao.realizar_transacao(conta_joao, saque_joao)

    deposito_maria = Deposito(500)
    cliente_maria.realizar_transacao(conta_maria, deposito_maria)

    saque_maria = Saque(200)
    cliente_maria.realizar_transacao(conta_maria, saque_maria)

    print(f"Saldo atual (João): R${conta_joao.saldo}")
    print("Histórico de transações (João): ")
    print(conta_joao.historico.transacoes)

    print(f"Saldo atual (Maria): R${conta_maria.saldo}")
    print("Histórico de transações (Maria): ")
    print(conta_maria.historico.transacoes)

if __name__ == "__main__":
    main()