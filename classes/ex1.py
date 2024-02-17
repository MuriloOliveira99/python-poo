# Crie uma classe Carro:
# Adicione atributos como modelo, cor, ano, e preço.
# Implemente métodos para exibir informações do carro e calcular o preço com desconto.


class Carro:
    """
    Classe para representar um carro.
    
    ...
    
    Atributos
    ---------
    nome : str
        nome do carro
    modelo : str
        modelo do carro
    cor : str
        cor do carro
    ano : int
        ano do carro
    preco : float
        preço do carro
    
    Métodos
    -------
    exibir_informacoes(self):
        exibe o nome, modelo, cor, ano e preco do carro
    aplicar_desconto(self, desconto: float):
        aplica n desconto no preço do carro
    """
    
    def __init__(self, 
                 nome: str, 
                 modelo: str, 
                 cor: str, 
                 ano: int, 
                 preco: float) -> None:
        """
        Constrói todos os atributos necessários para o objeto carro.
        
        Parâmetros
        ----------
            nome : str
                nome do carro
            modelo : str
                modelo do carro
            cor : str
                cor do carro
            ano : int
                ano do carro
            preco : float
                preço do carro
        """
        
        self.nome = nome
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco = preco
        
    def exibir_informacoes(self) -> None:
        """
        Exibe nome, modelo, cor, ano e preço do carro.
        
        Retorno
        -------
        None
        """
        print(f'Nome: {self.nome}\n'
              f'Modelo: {self.modelo}\n'
              f'Cor: {self.cor}\n'
              f'Ano: {self.ano}\n'
              f'Preço: {self.preco}')
        
    def aplicar_desconto(self, desconto: float) -> float:
        """
        Calcula e retorna o preço do carro com desconto
        
        Paramêtros
        ----------
        desconto : float
            valor do desconto
            
        Returno
        -------
        float
        """
        
        desconto = self.preco - (self.preco * (desconto / 100))
        return desconto


# Tudo que estiver dentro do if, não será executado na hora de importar este arquivo.py para outro arquivo.py
# if __name__ == "__main__":
#     ferrari = Carro('Ferrari', 'F8 Spider', 'Vermelha', 2023, 50.0)
#     ferrari.exibir_informacoes()
#     print(f'Preço com desconto: {ferrari.aplicar_desconto(10)}')
