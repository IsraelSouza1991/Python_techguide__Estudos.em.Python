import os

diretorio = os.chdir(input(str('Informe o diretório')))
print(f'Diretório atual: {os.getcwd()}')

nome_padrao = input('Qual o padrão de nomes de arquivos usar (sem a extensão)?')
sf = input('Informe o número do projeto')

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = nome_padrao + '-' + sf + '-' + str(contador)
        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)

print(f'\nArquivos renomeados.')
