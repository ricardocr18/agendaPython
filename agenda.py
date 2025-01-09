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

def editar_agenda(agenda):
    if agenda:
        print("\nSegue contatos para serem editados")
        ver_agenda(agenda)
        try:
            idx = int(input ("Digite o número do contato que deseja alterar: ")) -1
            if 0 <= idx < len(agenda):
                contato = agenda[idx]
                print (f"\nEditando o contato: {contato['Nome']}")

                novo_nome = input(f"Digite o novo nome (ou pressione Enter para manter '{contato['Nome']}'): ")
                novo_telefone = input(f"Digite o novo telefone (ou pressione Enter para manter '{contato['Telefone']}'): ")
                novo_email = input(f"Digite o novo email (ou pressione Enter para manter '{contato['Email']}'): ")

                contato['Nome'] = novo_nome if novo_nome else contato['Nome']
                contato['Telefone'] = novo_telefone if novo_telefone else contato['Telefone']
                contato['Email'] = novo_email if novo_email else contato['Email']

                print ("\nContato atualizado com sucesso")
            else:
                print ("\nNúmero inválido. Tente novamente")
        except ValueError:
            print ("\nPor favor, inisra um número válido")
    else:
        print("\nA agenda está vazia, 😞")
    return

def ver_favoritos(agenda):
    favoritos = [contato for contato in agenda if contato["Favorito"]]
    if favoritos:
        print ("\nSeus contatos favoritos:")
        for idx, contato in enumerate(favoritos, 1):
            print(f"{idx}.Nome: {contato['Nome']}, Telefon: {contato['Telefone']}, Email: {contato['Email']} ")       
    else:
        print("\nA Agenda está vazia, sem informações. 😞")    
    return

def marcar_favorito(agenda):
    if agenda:
        print ("n\Segue contatos para serem marcados como favoritos:")
        ver_agenda(agenda)
        try:
            idx = int(input("Digite o número do contato que deseja marcar como favorito: ")) - 1
            if 0 <= idx < len(agenda):
                agenda[idx]["Favorito"] = True
                print(f"\nContato '{agenda[idx]['Nome']}' marcado como favorito!")
            else:
                print("\nNúmero inválido. Tente novamente.")
        except ValueError:
            print("\nPor favor, insira um número válido.") 
    else:
        print("\nA agenda está vazia, 😞")
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