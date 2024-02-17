# Desenvolva uma classe ContaBancaria
# Inclua atributos como número da conta, titular e saldo.
# Forneça métodos para depositar, sacar e exibir o saldo.

class ContaBancaria():
    """
    Classe para representar uma conta bancaria.
    
    ...
    
    Atributos
    ---------
    numero_conta : str
        número da conta
    titular: str
        nome do títular
    saldo: float
        saldo da conta bancária
    
    Métodos
    -------
    depositar(self, valor: float):
        deposita n valor na conta bancária
    sacar(self, valor: float):
        saca n valor da conta bancária
    exibir(self):
        exibe o saldo da conta bancária
    """
    
    def __init__(self, numero_conta: int, titular: str, saldo: int = 0) -> None:
        """
        Constrói todos os atributos necessários para o objeto conta bancária.
        
        Parâmetros
        ----------
            numero_conta : str
                número da conta
            titular: str
                nome do títular
            saldo: float
                saldo da conta bancária
        """
        
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor: float) -> None:
        """
        Calcula e saca n valor da conta bancária do títular
        
        Paramêtros
        ----------
        valor : float
            valor do saque
            
        Returno
        -------
        None
        """
        
        self.saldo += valor
    
    def sacar(self, valor: float) -> None:
        """
        Calcula e saca n valor da conta bancária do títular
        
        Paramêtros
        ----------
        valor : float
            valor do saque
            
        Returno
        -------
        None
        """
        self.saldo -= valor
    
    def exibir_saldo(self) -> None:
        """
        Exibe o saldo da conta bancária do títular.
        
        Retorno
        -------
        None
        """
        print(f'Seu saldo atual é de R${self.saldo} reais')


# Tudo que estiver dentro do if, não será executado na hora de importar este arquivo.py para outro arquivo.py
# if __name__ == '__main__':
#     cb_murilo = ContaBancaria(7827852, 'Murilo Rocha', 1000.00)
#     cb_murilo.exibir_saldo()