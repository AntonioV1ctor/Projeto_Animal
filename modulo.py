from previwer import *



#-------------------------------INICIO CLASSES---------------------------------
class Animal:
    nome:str
    coracao:bool
    racionalidade:bool
    instinto:bool
    cultura:bool
    status_atual:list
    def __init__(self,nome,coracao,racionalidade,instinto,cultura,status_atual) -> None:
        self.nome=nome
        self.coracao=coracao
        self.racionalidade=racionalidade
        self.instinto=instinto
        self.cultura=cultura
        self.status_atual=status_atual


class Cachorro(Animal):
    def __init__(self,nome,cor,sexualidade,raca,peso) -> None:
        self.nome=nome
        self.cor=cor
        self.sexualidade=sexualidade
        self.raca=raca
        self.peso=peso
        self.coracao=True
        self.instinto=True
        self.racionalidade=False
        self.cultura=False
        self.status_atual=[]

    
class Humano(Animal):
    def __init__(self,nome,cor,sexualidade,raca,peso) -> None:
        self.nome=nome
        self.cor=cor
        self.sexualidade=sexualidade
        self.raca=raca
        self.peso=peso
        self.coracao=True
        self.instinto=True
        self.racionalidade=True
        self.cultura=True
        self.status_atual=[]

#--------------------------------FIM CLASSES--------------------------------






