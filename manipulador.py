# importa a biblioteca
import json

# classe arquivo Json
class Manipulador:
    def criar_arquivo(self, nome_arquivo):
        try:
            usuarios = [
                {
                    'Codigo': 0,
                    'Nome': 'Admin',
                    'CPF': '000.000.000-00',
                    'E-mail': 'admin@admin.com',
                    'Profissao': 'Administrador'
                }
            ]
            # serializando objeto python como json
            json_dados = json.dumps(usuarios)
            with open(f"{nome_arquivo}.json", 'w', encoding='utf-8') as f:
                f.write(json_dados)
            return f'{nome_arquivo}.json criado com sucesso!'
        except Exception as e:
            return f'Não foi possível criar o arquivo. {e}.'
        
    def abrir_arquivo(self, nome_arquivo):
        # transformar ou seja desserializando objeto json para pyrhon
        with open(f'{nome_arquivo}.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            return dados
        
    def salvar_dados(self, usuarios, nome_arquivo):
        try:
            with open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as f:
                json.dump(usuarios, f)
            return f'Dados gravados com sucesso!'
        except Exception as e:
            return f'Não foi possível salvar os dados. {e}.'
    
    def __del__(self):
        return 'Manipulador destruído!'