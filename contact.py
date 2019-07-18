#!/usr/bin/python 
# coding: utf-8

# # Project #1
# 
# Utilize conhecimentos adquiridos até aqui para criar um pequeno sistema para gravar contatos em um vetor.
# Cada posição do vetor deve conter um dicionário no formato a seguir:
# 
# ```py
# person = {
#     'nome': '',
#     'sobrenome': '',
#     'numero': '',
#     'email': ''
# }
# ```
# 
# Implemente funções para criar uma pessoa (`person`) no formato acima. Adicione condições para que uma pessoa sempre possua um nome, e um número ou um email.
# 
# Implemente uma função que imprima cada cotato da lista como segue os exemplos:
# 
# ```
# Johnson, Bob
# Contacts:
#  > 555-2368
#  > bob.johnson@example.com
#  
# Alice
# Contact:
#  > alice.madwoman@example.com
# ```
# Onde o primeiro exemplo contém todos os dados e o segundo contém apenas o nome e o email.
# 
# Segue o código base:

# In[ ]:


# Variáveis
contacts = []
options = {
    'add':    1,
    'remove': 2,
    'sort':   3,
    'print':  4,
    'save':   5,
    'exit':   9
}


# In[ ]:


def print_menu(length = 30):      
    print('Menu'.upper().center(30))
    print(('-'*25).center(30))
    
    for k,v in options.items():
        print(('{}:'.format(k.title()).ljust(20) + str(v)).center(30))
        
    print(('-'*25).center(30))


# In[ ]:


def create_contact(contacts):

    contato = {
        'nome': '',
        'sobrenome': '',
        'email': '',
        'numero': '',

    }
    

    while contato['nome'] == '':
        nome = input("Digite seu nome: ")


        if nome != '':
            nome = nome.split()
            contato['nome'] = nome[0]

            if len(nome) > 1:
                contato['sobrenome'] = nome[1]

    print(contato)
    
    return None


# In[ ]:


def add_contact(contacts):

    create_contact(contacts)
    '''
        Esta função cria e adiciona um contato ao fim do array de contatos.
        Cada contato possui a seguinte estrutura:
        
        person = {
            'nome': '',
            'sobrenome': '',
            'numero': '',
            'email': ''
        }
    '''




# In[ ]:


def remove_contact(contacts):
    ''' Esta função remove um contato utilizando o nome como pesquisa '''
    pass


# In[ ]:


def print_contacts(contacts):
    ''' Esta função imprime os contatos gera um contato com nome e um número de contato ou email '''
    pass


# In[ ]:


def sort_contacts(contacts):
    ''' Esta função ordena os contatos por nome e sobrenome '''
    pass


# In[ ]:


def save_contacts(contacts, file = '../../res/tmp.txt'):
    ''' Esta função salva os contatos em um arquivo. Utilize qualquer formato '''
    pass


# In[ ]:


# Main
if __name__ == '__main__':
    while True:
        # Menu
        print_menu()
            
        # Choosing Option
        opt = 0
        while opt not in options.values():
            opt = int(input('    > '))
            
        # Action
        if opt == 9:
            break
        elif opt == 1:
            print('Add'.upper().center(30))
            add_contact(contacts)
        elif opt == 2:
            print('Remove'.upper().center(30))
            remove_contact(contacts)
        elif opt == 3:
            print('Sort'.upper().center(30))
            sort_contacts(contacts)
        elif opt == 4:
            print('Print'.upper().center(30))
            print_contacts(contacts)
        elif opt == 5:
            print('Save'.upper().center(30))
            sort_contacts(contacts)
            save_contacts(contacts)
            
    print('Program ended'.upper().center(30))


# In[ ]:


help(add_contact)