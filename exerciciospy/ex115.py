import Módulos.lib.Interface
import Módulos.lib.arquivo
from time import sleep

arq = 'Módulos/lib/arquivo/pessoas.txt'

if not Módulos.lib.arquivo.arquivoExiste(arq):
    Módulos.lib.arquivo.CriarArquivo(arq)

while True:
    resposta = Módulos.lib.Interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair'])
    if resposta == 1:
        #opção de listar conteúdo do arquivo
        Módulos.lib.arquivo.listarArquivo(arq)
    elif resposta == 2:
        #cadastrar nova pessoa
        Módulos.lib.Interface.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = Módulos.lib.Interface.LeiaInt('Idade: ')
        Módulos.lib.arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        Módulos.lib.Interface.cabecalho('Saída do sistema, até logo!')
        break
    else:
        print('\033[31mOpção inválida. Tente novamente.\033[m')
    sleep(2)