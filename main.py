from modulo import *
from previwer import *

lista_cachorro=[]
lista_humano=[]

#-------------------------------CRIAR HUMANO--------------------------------
def criar_humano():
    nome=input("NOME:")
    cor=input("COR:")
    sexualidade=input("SEXUALIDADE:")
    raca=input("RAÇA:")
    peso=input("PESO:")
    _Humano=Humano(nome,cor,sexualidade,raca,peso)
    print("Humano Criado com sucesso!!!")
    pressione_enter()
    return _Humano

#-------------------------------FIM CRIAR HUMANO--------------------------------

#-------------------------------CRIAR CACHORRO----------------------------------
def criar_cachorro():
    nome=input("NOME:")
    cor=input("COR:")
    sexualidade=input("SEXUALIDADE:")
    raca=input("RAÇA:")
    peso=input("PESO:")
    cachorro=Cachorro(nome,cor,sexualidade,raca,peso)
    print("Cachorro Criado com sucesso!!!")
    pressione_enter()
    return cachorro

#-------------------------------FIM CRIAR CACHORRO-------------------------------




close=True
while close:
    limpar_tela()
    menu()
    opt_menu=input(">>>")
    if opt_menu == "1":
        cachorro=criar_cachorro()
        lista_cachorro.append(cachorro)
    elif opt_menu == "2":
        listar_dog(lista_cachorro)
    elif opt_menu == "3":
        humano = criar_humano()
        lista_humano.append(humano)
    elif opt_menu == "4":
        listar_humano(lista_humano)
    elif opt_menu == "5":
        selecionar_animal(lista_cachorro,lista_humano)
        #Mudar status atual. ai vai aparecer duas opções : mudar status de humano e mudar status de cachorro. Depois o usr vai ter que escolher a função atyal que vai ter na lista.
    elif opt_menu == "0":
        close=False
    else:
        print("Opção não Existente!")