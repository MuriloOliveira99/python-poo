# Herança com animais
# - Crie uma classe base Animal com atributos como nome e idade.
# - Derive classes específicas como Cachorro e Gato.
# - Adicione métodos que são específicos para cada tipo de animal.

class Animal:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

        
class Cachorro(Animal):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
    
    def latir(self) -> None:
        print('AU! AU! AU!')


class Gato(Animal):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
    
    def miar(self) -> None:
        print('MIAAAAAAAAAAU!!!')


## Tudo que estiver dentro do if, não será executado na hora de importar este arquivo.py para outro arquivo.py
# if __name__ == '__main__':
    
#     # Classe Animal
#     print('-' * 50)
#     animal = Animal('Classe Animal', 10)
#     print(animal.nome)
#     print(animal.idade)
#     print('-' * 50)

#     # Class Cachorro
#     cachorro = Cachorro('Caramelo', 12)
#     print(f'Nome: {cachorro.nome}')
#     print(f'Idade: {cachorro.idade}')
#     cachorro.latir()
#     print('-' * 50)

#     # Classe Cachorro
#     gato = Gato('Mustang', 5)
#     print(f'Gato: {gato.nome}')
#     print(f'Idade: {gato.idade}')
#     gato.miar()

#     print('-' * 50)
    
    
    

