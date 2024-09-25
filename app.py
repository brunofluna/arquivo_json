# importação de bibliotecas
import os
# importando as classes 
from pessoa import *
from manipulador import *

if __name__ == '__main__':
    # instanciando os objetos
    p = Pessoa(0,'','','','')
    m = Manipulador()

    while True:
        # Menu
        print('1 - Criar novo arquivo JSON.')
        print('2 - Abrir e ler arquivo JSON.')
        print('3 - Salvar novo usuário JSON.')
        print('4 - Alterar dados do usuário.')
        print('5 - Deletar usuário.')
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
                    #usuario = {}
                    #campos = ('nome', 'cpf','email', 'profissao')
                    #print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    #usuario['codigo'] = len(usuario)
                    #for campo in campos:
                    #    usuario[campo] = input(f'Digite o campo {campo.capitalize()}: ')
                    #usuarios.append(usuario)
                    #print(m.salvar_dados(usuario, abrir_arquivo))
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    p.codigo = len(usuarios)
                    p.nome = input('Informe o nome: ')
                    p.cpf = input('Informe o cpf: ')
                    p.email = input('Informe o email: ')
                    p.profissao = input('Informe a profissao: ')
                    usuario = dict(codigo=p.codigo, nome=p.nome, cpf=p.cpf, email=p.email, profissao=p.profissao) #dict outra forma de criar um dicionário
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuarios, abrir_arquivo))
                except Exception as e:
                    print(f'Não foi possível realizar a operação. {e}.')
                finally:
                    continue
            case '4':
                try:
                    print(f'Arquivo aberto: {abrir_arquivo}.json. \n')
                    codigo = int(input('Digite o código do usuário que deseja alterar os dados: '))
                    for campo in usuarios[codigo]:
                        print(f'Valor atual do campo {campo}: {usuarios[codigo].get(campo)}')
                        novo_dado = input(f'Digite o novo dado do campo {campo} ou aperte "Enter" caso deseje manter o mesmo valor: ')
                        if novo_dado:
                            usuarios[codigo][campo] = novo_dado
                        else:
                            ...
                    print(m.salvar_dados(usuarios, abrir_arquivo))
                except Exception as e:
                    print(f'Não foi possível alterar os dados. {e}.')
                finally:
                    continue
            case '5':
                try:
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    codigo = int(input('Digite o código do usuário que deseja deletar: '))
                    nome_deletado = usuarios[codigo]['nome']
                    confirmacao = input(f'Deseja deletar o usuário {nome_deletado}? \nDigite "SIM" para confirmar: ').upper()
                    if confirmacao == "SIM":
                        del(usuarios[codigo])
                        print(m.salvar_dados(usuarios, abrir_arquivo))
                        print(f'Usuário {nome_deletado} deletado com sucesso.')
                    else:
                        print(f'Usuário {nome_deletado} não foi excluído.')
                except Exception as e:
                    print(f"Não foi possível deletar o arquivo. {e}.")
                finally:
                    continue
            case _:
                print('Opção inválida!')
                continue