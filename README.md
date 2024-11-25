# Inovar IADEPG

Este projeto tem como objetivo criar uma IA capaz de gerar códigos e programas em várias linguagens, com foco especial em desenvolvimento Android, incluindo geração de código Kotlin e layouts XML.

## Estrutura do Projeto

- `code_generation_model.py`: Contém o modelo de geração de código que suporta múltiplas linguagens, componentes Android e layouts XML usando a biblioteca Transformers.
- `cli.py`: Interface de linha de comando para interagir com o modelo de geração de código.
- `gui.py`: Interface gráfica do usuário para interagir com o modelo de geração de código.

## Progresso

- [x] Criação do modelo básico de geração de código
- [x] Expansão para múltiplas linguagens (Python, Java, JavaScript, Kotlin)
- [x] Implementação de suporte avançado para desenvolvimento Android
- [x] Criação de interface de linha de comando (CLI)
- [x] Melhoria na qualidade e relevância do código gerado para Android
- [x] Adição de suporte para geração de layouts XML para Android
- [x] Implementação de uma interface gráfica de usuário (GUI)

## Como usar

### Interface Gráfica (GUI)

1. Certifique-se de ter Python 3.7+ instalado.
2. Instale as dependências:
   ```
   pip install transformers torch
   ```
3. Execute o script GUI:
   ```
   python gui.py
   ```
4. Use a interface gráfica para selecionar a linguagem, o componente Android (se aplicável) e inserir o prompt para gerar o código.

### Interface de Linha de Comando (CLI)

1. Use a CLI para gerar código:
   ```
   python cli.py --language python --prompt "def fibonacci(n):"
   python cli.py --language kotlin --android activity
   python cli.py --language xml --android-layout activity
   ```

### Online

Você pode executar este programa online usando as seguintes plataformas:

1. [Google Colab](https://colab.research.google.com/): Faça o upload dos arquivos `code_generation_model.py`, `cli.py`, e `gui.py`, e execute-os em um notebook.
2. [Repl.it](https://replit.com/): Crie um novo projeto Python, copie o conteúdo dos arquivos e execute-os.
3. [Binder](https://mybinder.org/): Crie um ambiente Jupyter a partir deste repositório GitHub.

## Linguagens Suportadas

- Python
- Java
- JavaScript
- Kotlin
- XML (para layouts Android)

## Funcionalidades de Desenvolvimento Android

O modelo agora suporta:

1. Geração avançada dos seguintes componentes Android com templates detalhados:
   - Activity
   - Fragment
   - Service
   - BroadcastReceiver

2. Geração de layouts XML para Android:
   - Layout de Activity
   - Layout de Fragment
   - Layout de item de lista

## Próximos Passos

- Melhorar a interface gráfica do usuário (GUI) com mais opções e personalização
- Adicionar suporte para mais padrões de design e arquiteturas Android (MVVM, Clean Architecture, etc.)
- Implementar testes unitários e de integração
- Explorar a possibilidade de fine-tuning do modelo para melhorar ainda mais a qualidade do código gerado
- Adicionar suporte para geração de recursos Android (strings, cores, estilos, etc.)

## Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter pull requests ou abrir issues para sugerir melhorias ou reportar bugs.

