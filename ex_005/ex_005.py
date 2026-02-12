'''
Desafio 017

Crie a classe Produto, 
onde podemos cadastrar nome e o preço.
Crie também um método que mostre uma
etiqueta de preço do produto.
'''

from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    
    def etiqueta(self):
        larg = 28
        nome = self.nome.center(larg)
        meio = "-" * larg
        preco = f"R${self.preco:,.2f}".center(larg, "-")
        conteudo = f"{nome}\n{meio}\n{preco}"
        etiqueta = Panel(conteudo, title="Produto")
        return etiqueta


terco = Produto("Terço", 25)
mouse = Produto("Mouse", 100)
iphone = Produto("Iphone 17 Pro Max", 25_000.85)
print(terco.etiqueta())
print(mouse.etiqueta())
print(iphone.etiqueta())