# Relacionamento (Associação) entre Classes
# - Crie uma classe Estudante e uma classe Curso.
# - Estabeleça um relacionamento onde um curso pode ter vários estudantes.

class Estudante:
    def __init__(self, ra: int, nome: str) -> None:
        self.nome = nome
        self.ra = ra
        
    
class Curso:
    def __init__(self, id: int, curso: str) -> None:
        self.curso = curso
        self.id = id
        self.lista_estudantes = []
    
    def add_estudante(self, estudante: Estudante) -> None:
        self.lista_estudantes.append(estudante)


## Tudo que estiver dentro do if, não será executado na hora de importar este arquivo.py para outro arquivo.py
# if __name__ == "__main__":        
#     estudante1 = Estudante(9329, 'Murilo')
#     estudante2 = Estudante(8491, 'Oliveira')
#     estudante3 = Estudante(5121, 'Rocha')
#     estudante4 = Estudante(8952, 'Marcolino')

#     python = Curso(1, 'Python')
#     sql = Curso(2, 'SQL')
#     spark = Curso(3, 'Spark')

#     python.add_estudante(estudante3)
#     sql.add_estudante(estudante1)
#     spark.add_estudante(estudante2)
#     python.add_estudante(estudante4)

#     # Lista os estudantes do curso1
#     for estudante in python.lista_estudantes:
#         print(estudante.nome)

