import os
import sys
from datetime import datetime

def concatenar_arquivos(nome_arquivo_saida):
    """
    Concatena todos os arquivos .txt no diretório atual em um único arquivo.

    Args:
    nome_arquivo_saida (str): Nome do arquivo de saída onde o conteúdo será concatenado.
    """
    # Obtém o diretório atual
    diretorio_atual = os.getcwd()

    # Lista todos os arquivos .txt no diretório atual
    arquivos_txt = [f for f in os.listdir(diretorio_atual) if f.endswith('.txt') and f != nome_arquivo_saida]

    # Ordena os arquivos por data de modificação (do mais antigo para o mais novo)
    arquivos_txt.sort(key=lambda x: os.path.getmtime(os.path.join(diretorio_atual, x)))

    # Abre o arquivo de saída para escrita
    with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        for nome_arquivo in arquivos_txt:
            # Escreve o nome do arquivo
            arquivo_saida.write(f"{nome_arquivo}\n")
            arquivo_saida.write("===\n")

            # Lê e escreve o conteúdo do arquivo
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_entrada:
                conteudo = arquivo_entrada.read()
                arquivo_saida.write(conteudo)

            # Adiciona uma quebra de linha extra após o conteúdo de cada arquivo
            arquivo_saida.write("\n\n")

    print(f"Arquivo '{nome_arquivo_saida}' criado com sucesso!")

def main():
    """
    Função principal que processa os argumentos da linha de comando e chama concatenar_arquivos().
    """
    if len(sys.argv) != 2:
        print("Uso: txtconcat nome_arquivo_saida.txt")
        sys.exit(1)

    nome_arquivo_saida = sys.argv[1]
    concatenar_arquivos(nome_arquivo_saida)

if __name__ == "__main__":
    main()
