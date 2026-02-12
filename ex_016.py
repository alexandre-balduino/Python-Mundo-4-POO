'''
Desafio 016

Crie a classe Funcionario, 
onde podemos cadastrar nome, 
setor e cargo. 
Crie tambem um método que permita 
ao funcionário se apresentar.
'''

from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = "Curso em Vídeo"
    
    
    def apresentar(self):
        return f":wave: Olá, sou [blue] {self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {self.empresa}"


maria = Funcionario("Maria", "Administração", "Diretora")
pedro = Funcionario("Pedro", "TI", "Programador")
alexandre = Funcionario("Alexandre", "Artesanato", "Fazedor de Terços")
alexandre.empresa = "Terços da Imaculada"
print(maria.apresentar())
print(pedro.apresentar())
print(alexandre.apresentar())
