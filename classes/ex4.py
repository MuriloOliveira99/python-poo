# - Crie uma classe Pessoa com atributos como nome, idade e número de telefone.
# - Encapsule os atributos usando métodos getters e setters.

class Pessoa:
    def __init__(self, nome: str, idade: int, numero_telefone: str = '00 00000-0000') -> None:
        self.__nome = nome
        self.__idade = idade
        self.__numero_telefone = numero_telefone
    
    # get
    @property
    def nome(self) -> str:
        return self.__nome
    
    # set    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome
        
    @property
    def idade(self) -> int:
        return self.__idade
    
    @idade.setter
    def idade(self, idade: int) -> None:
        self.__idade = idade
        
    @property
    def numero_telefone(self) -> str:
        return self.__numero_telefone
    
    @numero_telefone.setter
    def numero_telefone(self, num_telefone: str) -> None:
        self.__numero_telefone = num_telefone
    
    
# if __name__ == "__main__":
#     p1 = Pessoa('Murilo', 24, '00 00000-0000')
#     print(p1.nome) # get
#     print(p1.idade) # get
#     print(p1.numero_telefone) # get
#     print()
#     p1.nome = 'Rocha' # setter
#     p1.idade = 20 # setter
#     p1.numero_telefone = '99 99999-9999' # setter
#     print(p1.nome) # get
#     print(p1.idade) # get
#     print(p1.numero_telefone) # get