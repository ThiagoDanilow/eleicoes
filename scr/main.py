import pickle
import traceback

from common import *

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

def menu_principal():
    print("1 - Gerenciar Eleitores")
    print("2 - Gerenciar Candidatos")
    print("3 - Sair")
    op = int(input("Digite a opção [1,2,3]: "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opção [1,2,3]: "))
    return op

def menu_eleitor():
    print("1 - Novo Eleitor")
    print("2 - Atualizar Eleitor")
    print("3 - Voltar")
    op = int(input("Digite a opção [1,2,3]: "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opção [1,2,3]: "))
    return op

def menu_candidato():
    print("1 - Novo Candidato")
    print("2 - Atualizar Candidato")
    print("3 - Voltar")
    op = int(input("Digite a opção [1,2,3]: "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opção [1,2,3]: "))
    return op

def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Título: "))

    if titulo in eleitores:
        raise Exception("Título já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    secao = input("Digite a seção: ")
    zona = input("Digite a zona: ")

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

    print('Eleitor gravado com sucesso!')
    print(eleitor)

def atualizar_eleitor(eleitores):
    titulo = int(input('Digite o título do eleitor: '))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
        secao = input("Digite a nova seção: ")
        zona = input("Digite a nova zona: ")
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Dados do eleitor atualizados!')
        print(eleitor)
    else:
        raise Exception('Título inexistente')

def inserir_candidato(candidatos):
    numero = int(input("Digite o número do candidato: "))

    if numero in candidatos:
        raise Exception("Número já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    partido = input("Digite o partido: ")
    cargo = input("Digite o cargo: ")

    candidato = Candidato(nome, RG, CPF, numero, partido, cargo)
    candidatos[candidato.get_numero()] = candidato

    with open(FILE_CANDIDATOS, 'wb') as arquivo:
        pickle.dump(candidatos, arquivo)

    print('Candidato gravado com sucesso!')
    print(candidato)

def atualizar_candidato(candidatos):
    numero = int(input('Digite o número do candidato: '))

    if numero in candidatos:
        candidato = candidatos[numero]
        print(candidato)
        partido = input("Digite o novo partido: ")
        cargo = input("Digite o novo cargo: ")
        candidato.partido = partido
        candidato.cargo = cargo

        with open(FILE_CANDIDATOS, 'wb') as arquivo:
            pickle.dump(candidatos, arquivo)

        print('Dados do candidato atualizados!')
        print(candidato)
    else:
        raise Exception('Número inexistente')

if __name__ == "__main__":
    eleitores = {}
    candidatos = {}

    try:
        print("Carregando arquivos...")

        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo de eleitores não encontrado, nenhum eleitor carregado!")

    try:
        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            candidatos = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo de candidatos não encontrado, nenhum candidato carregado!")

    opcao = 1
    while opcao in (1, 2, 3):
        try:
            opcao = menu_principal()

            if opcao == 1:
                opcao_eleitor = 1
                while opcao_eleitor in (1, 2, 3):
                    opcao_eleitor = menu_eleitor()

                    if opcao_eleitor == 1:
                        inserir_eleitor(eleitores)
                    elif opcao_eleitor == 2:
                        atualizar_eleitor(eleitores)
                    elif opcao_eleitor == 3:
                        print("Voltando ao menu principal.")
                        break

            elif opcao == 2:
                opcao_candidato = 1
                while opcao_candidato in (1, 2, 3):
                    opcao_candidato = menu_candidato()

                    if opcao_candidato == 1:
                        inserir_candidato(candidatos)
                    elif opcao_candidato == 2:
                        atualizar_candidato(candidatos)
                    elif opcao_candidato == 3:
                        print("Voltando ao menu principal.")
                        break

            elif opcao == 3:
                print("Saindo!")
                break

        except Exception as e:
            # traceback.print_exc()
            print(e)
