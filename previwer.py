import os
import time

def limpar_tela():
    os.system("cls")

def pressione_enter():
    input("Pressione Enter para Continuar...")
    time.sleep(0.1)
    limpar_tela()

def menu():
    print("""
+============================+
 | [1]-Criar Cachorro       |
 | [2]-Listar Cachorro      |
 [==========================]
 | [3]-Criar Humano         |
 | [4]-Listar Humano        |
 [==========================]
 | [5]-Mudar status atual   |
 | [0]-Sair                 |
+============================+""")
    
def listar_humano(Lista_Humano):
    for i in Lista_Humano:
        print("+========================+")
        print(f" |Nome:{i.nome}")
        print("+========================+")
        print(f" |COR:{i.cor}")
        print(f" |SEXUALIDADE:{i.sexualidade}")
        print(f" |RAÇA:{i.raca}")
        print(f" |PESO:{i.peso} Kg")
        print(f" |CORAÇÃO:{i.coracao}")
        print(f" |RACIONALIDADE:{i.racionalidade}")
        print(f" |INSTINTO:{i.instinto}")
        print(f" |CULTURA:{i.cultura}")
        print(f" |Status Atual:{i.status_atual}")
        print("+========================+")
        pressione_enter()


def listar_dog(Lista_Cachorro):
    for i in Lista_Cachorro:
        print("+========================+")
        print(f" |Nome:{i.nome}")
        print("+========================+")
        print(f" |COR:{i.cor}")
        print(f" |SEXUALIDADE:{i.sexualidade}")
        print(f" |RAÇA:{i.raca}")
        print(f" |PESO:{i.peso} Kg")
        print(f" |CORAÇÃO:{i.coracao}")
        print(f" |RACIONALIDADE:{i.racionalidade}")
        print(f" |INSTINTO:{i.instinto}")
        print(f" |CULTURA:{i.cultura}")
        print(f" |Status Atual:{i.status_atual}")
        print("+========================+")
        pressione_enter()


#professor Rafael, só para deixar claro eu não estou usando nem um tipo sequer de I.A 
#Esses comentários pelo código são frutos da minha mente e esquisofrenia 😞
#Brincadeiras a parte é só para eu me organizar e não esquecer o que era para fazer 👌

#Adicionar 2 funções 
"""
latir
andar
comer
beber agua
"""
def selecionar_animal(Lista_Cachorro,Lista_Humano):
    #Escolher entre Cachorro ou Humano.
    especies_animais()
    opt_menu=input(">>>")
    if opt_menu == "1":
        for x in range(0,len(Lista_Cachorro)):        
            print(f"[{x}]-{Lista_Cachorro[x].nome}")

        selecionar_cao=int(input("Digite qual Animal você vai mudar o Status Atual:"))
        menu_funcoes()
        selecionar_funcoes=input(">>>")

        if selecionar_funcoes == "1":
            limpar_tela()
            Lista_Cachorro[selecionar_cao].status_atual=["Bebendo Agua"]
            print(f"O cachorro {Lista_Cachorro[selecionar_cao].nome} Esta Bebendo Agua!!")
            pressione_enter()

        elif selecionar_funcoes == "2":
            limpar_tela()
            Lista_Cachorro[selecionar_cao].status_atual=["Comendo"]
            print(f"O cachorro {Lista_Cachorro[selecionar_cao].nome} Esta Comendo!!")
            pressione_enter()

        elif selecionar_funcoes == "3":
            limpar_tela()
            Lista_Cachorro[selecionar_cao].status_atual=["Latindo"]
            print(f"O cachorro {Lista_Cachorro[selecionar_cao].nome} Esta Latindo")
            pressione_enter()

        elif selecionar_funcoes == "4":
            limpar_tela()
            Lista_Cachorro[selecionar_cao].status_atual=["Andando"]
            print(f"O cachorro {Lista_Cachorro[selecionar_cao].nome} Esta Andando")
            pressione_enter()
        else:
            print("Opção Errada!!")
            pressione_enter()
            pass

    elif opt_menu == "2":
        
        for x in range(0,len(Lista_Humano)):
            print(f"[{x}]-{Lista_Humano[x].nome}")
        
        selecionar_humano=int(input("Digite qual Animal você vai mudar o Status Atual:"))
        menu_funcoes()
        selecionar_funcoes=input(">>>")
        
        if selecionar_funcoes == "1":
            limpar_tela()
            Lista_Humano[selecionar_humano].status_atual=["Bebendo Agua"]
            print(f"O Humano {Lista_Humano[selecionar_humano].nome} Esta Bebendo Agua!!")
            pressione_enter()

        elif selecionar_funcoes == "2":
            limpar_tela()
            Lista_Humano[selecionar_humano].status_atual=["Comendo"]
            print(f"O Humano {Lista_Humano[selecionar_humano].nome} Esta Comendo!!")
            pressione_enter()

        elif selecionar_funcoes == "3":
            limpar_tela()
            print(f"Pra que o {Lista_Humano[selecionar_humano].nome} ia Latir kkkkk????")
            pressione_enter()

        elif selecionar_funcoes == "4":
            limpar_tela()
            Lista_Humano[selecionar_humano].status_atual=["Andando"]
            print(f"O Humano {Lista_Humano[selecionar_humano].nome} Esta Andando")
            pressione_enter()

        else:
            print("Opção Errada!!")
            pressione_enter()
            pass

    elif opt_menu == "0":
        pressione_enter()
        pass

    else:
        print("Opção Errada!!")
        pressione_enter()
        pass

def especies_animais():
    print("""
+=========================================+
 | [1]-Cachorro                          |
 | [2]-Humano                            |
 | [0]-Voltar para o Menu                |
+=========================================+""")


def menu_funcoes():
    print("""
+=========================================+
 | [1]-Beber Agua                        |
 | [2]-Comer                             |
 | [3]-Latir                             |
 | [4]-Andar                             |
+=========================================+""")