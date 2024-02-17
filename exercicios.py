# DOCSTRING: https://www.programiz.com/python-programming/docstrings
# Programador Lhama: https://www.youtube.com/watch?v=WP5p4QEqLLQ&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_

from os import system
system('cls')

from classes.ex1 import Carro
from classes.ex2 import ContaBancaria
from classes.ex3 import (Animal, 
                         Cachorro, 
                         Gato)
from classes.ex4 import Pessoa


""" EXERCÍCIO 01: Crie uma classe Carro:
- Adicione atributos como modelo, cor, ano, e preço.
- Implemente métodos para exibir informações do carro e calcular o preço com desconto.
"""
print('+' * 40 + '\n- Exercício 01:\n' + '+' * 40)
ferrari = Carro('Ferrari', 'F8 Spider', 'Vermelha', 2023, 50.0)
ferrari.exibir_informacoes()
print(f'Preço com desconto: {ferrari.aplicar_desconto(10)}')
print()


""" EXERCÍCIO 02: Desenvolva uma classe ContaBancaria
- Inclua atributos como número da conta, titular e saldo.
- Forneça métodos para depositar, sacar e exibir o saldo.
"""
print('+' * 40 + '\n- Exercício 02:\n' + '+' * 40)
cb_murilo = ContaBancaria(7827852, 'Murilo Rocha', 1000.00)
cb_murilo.exibir_saldo()
print()


""" EXERCÍCIO 03: Herança com animais
- Crie uma classe base Animal com atributos como nome e idade.
- Derive classes específicas como Cachorro e Gato.
- Adicione métodos que são específicos para cada tipo de animal.
"""
# Classe Animal
print('+' * 40 + '\n- Exercício 03:\n' + '+' * 40)
animal = Animal('Classe Animal', 10)
print(animal.nome)
print(animal.idade)
print()

# Class Cachorro
cachorro = Cachorro('Caramelo', 12)
print(f'Nome: {cachorro.nome}')
print(f'Idade: {cachorro.idade}')
cachorro.latir()
print()

# Classe Cachorro
gato = Gato('Mustang', 5)
print(f'Gato: {gato.nome}')
print(f'Idade: {gato.idade}')
gato.miar()
print()


""" EXERCÍCIO 04: Encapsulamento
- Crie uma classe Pessoa com atributos como nome, idade e número de telefone.
- Encapsule os atributos usando métodos getters e setters.
"""
print('+' * 40 + '\n- Exercício 04:\n' + '+' * 40)
p1 = Pessoa('Murilo Oliveira', 24, '99 99999-9999')
print(p1.nome) # get
print(p1.idade) # get
print(p1.numero_telefone) # get
print()

p1.nome = 'Murilo Rocha' # set
p1.idade = 20 # set
p1.numero_telefone = '11 11111-1111' # set

print(p1.nome) # get
print(p1.idade) # get
print(p1.numero_telefone) # get


""" EXERCÍCIO 05: Polimorfismo
- Crie uma interface FormaGeometrica com métodos como calcularArea e calcularPerimetro.
- Implemente classes como Circulo, Quadrado e Triangulo que implementam essa interface.
"""


"""EXERCÍCIO 06: Relacionamento (Associação) entre Classes
- Crie uma classe Estudante e uma classe Curso.
- Estabeleça um relacionamento onde um curso pode ter vários estudantes.
"""


"""EXERCÍCIO 07: Sistema de biblioteca
- Crie classes para representar Livro, Autor e Biblioteca.
- Relacione essas classes para que seja possível saber quais autores escreveram quais livros, e quantos exemplares a biblioteca possui.
"""

"""EXERCÍCIO 08: Sistema de funcionários:
- Crie classes para representar Empregado, Gerente e CEO.
- Use herança para representar a relação entre essas classes.
"""