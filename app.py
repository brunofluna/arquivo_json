# importação de bibliotecas
import os
# importando as classes 
from pessoa import *
from manipulador import *

if __name__ == '__main__':
    # instancia dos objetos
    p = Pessoa(0,'','','','')
    m = Manipulador()

    while True:
        # Menu
        print('1 - Criar novo arquivo JSON.')
        print('2 - Abrir e ler arquivo JSON.')
        print('3 - Salvar novo usuário JSON.')
        print('0 - Sair do programa.')

        opcao = input("Digite a opção desejada: ")

        # limpeza de console
        os.system('cls')
        match opcao:
            case '0':
                #print('Programa encerrado!')
                break
            case '1':
                novo_arquivo = input('Digite o nome do arquivo que deseja criar: ')
                print(m.criar_arquivo(novo_arquivo))
                continue
            case '2':
                abrir_arquivo = input('Digite o nome do arquivo que deseja abrir: ')
                try:
                    os.system('cls')
                    usuarios = m.abrir_arquivo(abrir_arquivo)
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    for i in range(len(usuarios)):
                        for campo in usuarios[i]:
                            print(f'{campo.capitalize()}: {usuarios[i].get(campo)}.')
                        print(f'\n{'-'*30}\n')
                except Exception as e:
                    print(f'Não foi possível abrir o arquivo. {e}.')
                finally:
                    continue
            case '3':
                try:
                    usuario = {}
                    campos = ('nome', 'cpf','email', 'profissao')
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    usuario['codigo'] = len(usuario)
                    for campo in campos:
                        usuario[campo] = input(f'Digite o campo {campo.capitalize()}: ')
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuario, abrir_arquivo))
                except Exception as e:
                    print(f'Não foi possível realizar a operação. {e}.')
                finally:
                    continue
            case _:
                print('Opção inválida!')
                continue