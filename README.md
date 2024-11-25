# Inovar IADEPG

Este projeto tem como objetivo criar uma IA capaz de gerar códigos e programas em várias linguagens, incluindo desenvolvimento Android.

## Estrutura do Projeto

- `code_generation_model.py`: Contém o modelo de geração de código que suporta múltiplas linguagens e componentes Android usando a biblioteca Transformers.
- `cli.py`: Interface de linha de comando para interagir com o modelo de geração de código.

## Progresso

- [x] Criação do modelo básico de geração de código
- [x] Expansão para múltiplas linguagens (Python, Java, JavaScript, Kotlin)
- [x] Implementação de suporte básico para desenvolvimento Android
- [x] Criação de interface de linha de comando (CLI)

## Como usar

### Localmente

1. Certifique-se de ter Python 3.7+ instalado.
2. Instale as dependências:
   ```
   pip install transformers torch
   ```
3. Use a CLI para gerar código:
   ```
   python cli.py --language python --prompt "def fibonacci(n):"
   python cli.py --language kotlin --android activity
   ```

### Online

Você pode executar este programa online usando as seguintes plataformas:

1. [Google Colab](https://colab.research.google.com/): Faça o upload dos arquivos `code_generation_model.py` e `cli.py`, e execute-os em um notebook.
2. [Repl.it](https://replit.com/): Crie um novo projeto Python, copie o conteúdo dos arquivos e execute-os.
3. [Binder](https://mybinder.org/): Crie um ambiente Jupyter a partir deste repositório GitHub.

## Linguagens Suportadas

- Python
- Java
- JavaScript
- Kotlin

## Funcionalidades de Desenvolvimento Android

O modelo suporta a geração básica dos seguintes componentes Android:

- Activity
- Fragment
- Service
- BroadcastReceiver

## Exemplos de Uso da CLI

1. Gerar código Python:
   ```
   python cli.py --language python --prompt "def fibonacci(n):"
   ```

2. Gerar uma Activity Android em Kotlin:
   ```
   python cli.py --language kotlin --android activity
   ```

## Próximos Passos

- Melhorar a qualidade e relevância do código gerado
- Adicionar suporte para mais componentes e padrões de desenvolvimento Android
- Implementar uma interface gráfica de usuário (GUI)
- Implementar testes unitários e de integração

## Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter pull requests ou abrir issues para sugerir melhorias ou reportar bugs.

