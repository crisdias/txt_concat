# TXTConcat

TXTConcat é uma ferramenta de linha de comando para concatenar arquivos TXT em um único arquivo. Ela percorre todos os arquivos .txt no diretório atual, do mais antigo para o mais novo, e combina seus conteúdos em um novo arquivo.

## Exemplo

Suponha que você tenha a seguinte estrutura de diretório:

```
diretorio_atual/
├── foo.txt
├── bar.txt
└── baz.txt
```

Com os seguintes conteúdos:

**foo.txt:**
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
```

**bar.txt:**
```
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
```

**baz.txt:**
```
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.
```

Ao executar o comando:

```
txtconcat resultado.txt
```

Será criado um novo arquivo `resultado.txt` com o seguinte conteúdo:

```
foo.txt
===
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

bar.txt
===
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

baz.txt
===
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.

```

## Instalação

### Opção 1: Instalação a partir do repositório clonado

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/txtconcat.git
   cd txtconcat
   ```

2. Instale as dependências necessárias:
   ```
   pip install build
   ```

3. Construa o pacote:
   ```
   python -m build
   ```

4. Instale o pacote:
   ```
   pip install .
   ```

## Uso

Após a instalação, você pode usar o TXTConcat de qualquer lugar no seu sistema:

```
txtconcat nome_arquivo_saida.txt
```

Este comando irá concatenar todos os arquivos TXT no diretório atual (exceto o arquivo de saída) em um novo arquivo chamado `nome_arquivo_saida.txt`.

## Desenvolvimento

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie sua branch de feature (`git checkout -b feature/AmazingFeature`)
3. Faça commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Distribuído sob a Licença MIT.
