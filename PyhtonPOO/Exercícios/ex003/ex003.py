class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo = 0):  # pyright: ignore[reportUnknownParameterType]
        self.id = id                          # pyright: ignore[reportUnannotatedClassAttribute]
        self.titular = nome               # pyright: ignore[reportUnannotatedClassAttribute]
        self.saldo = saldo               # pyright: ignore[reportUnannotatedClassAttribute]
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:.2f}')

    def __str__(self):                    # pyright: ignore[reportImplicitOverride]
        return f'A conta com ID {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo'  # pyright: ignore[reportUnknownMemberType]
    
    def deposito(self, valor):                  # pyright: ignore[reportUnknownParameterType]
        self.saldo += valor                   # pyright: ignore[reportUnknownMemberType]
        print(f'Depósito de R${valor:.2f} autorizado na conta {self.id}')

    def saque(self, valor):                     # pyright: ignore[reportUnknownParameterType]
        if valor > self.saldo:  # pyright: ignore[reportUnknownMemberType]
            print(f'Saque de R${valor:.2f} NEGADO. Saldo insuficiente.')
        else:
            self.saldo -= valor          # pyright: ignore[reportUnknownMemberType]             
            print(f'Saque de R$ {valor:.2f} autorizado na conta {self.id}')

c1 = ContaBancaria(110, 'Guilherme', 1000)
c1.deposito(500)                             # pyright: ignore[reportUnknownMemberType]
c1.saque(10_000)                                 # pyright: ignore[reportUnknownMemberType]
print(c1)