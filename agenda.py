def add_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input ("Digite o numero do telefone do contato: ")
    email = input ("Digite o email do contato: ")

    contato = {"Nome": nome,"Telefone": telefone, "Email": email, "Favorito": False}
    agenda.append(contato)
    print("\nContato adicionado com sucesso. 😉")
    return

def ver_agenda(agenda):
    if agenda:
            print("\nSeus contatos:")
            for idx, contato in enumerate(agenda, 1):
                print(f"{idx}. Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']}")
    else:
        print("\nA agenda está vazia.")
    return

# Lista inicial da agenda   
agenda = []

while True:
    print ("\nMenu do Gerenciador de Agenda 📑:\n")    
    print ("1. Adicione um contado")
    print ("2. Ver contatos")
    print ("3. Editar Contato")
    print ("4. Ver sua lista de Favoritos")
    print ("5. Marcar um contato como Favorito")
    print ("6. Desmarcar um contato como Favorito")
    print ("7. Deletar contatos da agenda")
    print ("8. Sair\n")

    escolha = input ("Escolha uma opção, por favor: ")

    if escolha == "1":
        add_contato(agenda)
    
    elif escolha == "2":
        ver_agenda(agenda)
    
    elif escolha == "3":
        editar_agenda(agenda)
    
    elif escolha == "4":
        ver_favoritos(agenda)
    
    elif escolha == "5":
        marcar_favorito(agenda)

    elif escolha == "6":
        desmarcar_favorito(agenda)
    
    elif escolha == "7":
        delete_contato(agenda)

    elif escolha == "8":
        print("\nPrograma finalizado. Até logo!")
        break

    else:
        print ("Programa Agenda, finalizada")