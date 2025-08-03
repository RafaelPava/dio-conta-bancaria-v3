# dio-conta-bancaria-v3

<img alt="Rafael" src="https://avatars.githubusercontent.com/u/144845857?v=4" width=70px height=70px>

## Rafael Inocente Pavão

Desafio da conta bancária v3 da [DIO](https://web.dio.me)

Implementação de um sistema bancário utilizando **Programação Orientada a Objetos (POO)**. O projeto foi desenvolvido com os conceitos de encapsulamento, herança, polimorfismo e uso de classes abstratas.

---

### 🚀 Funcionalidades

- Cadastro de **clientes Pessoa Física**
- Criação de contas **corrente** vinculadas aos clientes
- Depósitos e saques com **regras de validação**
- **Registro de histórico** de transações por conta
- Controle de **limite de valor por saque**
- Controle de **quantidade de saques por conta**
- Impressão de **extrato** com date e hora

---

### 🧱 Estrutura do projeto

- `Cliente`, `PessoaFisica`: estrutura base dos usuários
- `Conta`, `ContaCorrente`: classes de conta bancária com regras de negócio
- `Transacao` (classe abstrata), `Saque`, `Deposito`: modelam e registram operações financeiras
- `Historico`: registra todas as transações com data e hora
- `main()`: ponto de entrada do programa, com execução de cenários de teste

---

### ✅ Regras

- Depósito **não pode ser negativo**
- Limite de **3 saques diários**
- Limite de **R$ 500,00 por saque**
- O sistema impede **saques acima do saldo**
- Extrato exibe todas as **operações do dia**
- Transações implementadas com **classes abstratas e herança**
- Cada conta é criada com **número incremental** a partir de 1
- O cliente pode ter **múltiplas contas**
- Uso de **composição** entre cliente, conta e histórico
