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
- [x] Adição de funcionalidade para salvar o código gerado em um arquivo
- [x] Implementação de um histórico de códigos gerados na GUI
- [x] Adição de opções para personalizar os parâmetros de geração (temperatura, max_length)

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
4. Use a interface gráfica para:
   - Selecionar a linguagem
   - Escolher o componente Android (se aplicável)
   - Inserir o prompt para gerar o código
   - Ajustar os parâmetros de geração (temperatura e max_length)
5. Clique em "Generate Code" para gerar o código
6. Após gerar o código, você pode salvá-lo em um arquivo usando o botão "Save Code"
7. Use o botão "Show History" para ver e reutilizar códigos gerados anteriormente

#### Parâmetros de Geração

- **Temperatura**: Controla a aleatoriedade do código gerado. Valores mais baixos (ex: 0.2) produzem resultados mais determinísticos, enquanto valores mais altos (ex: 0.8) produzem resultados mais diversos e potencialmente mais criativos.
- **Max Length**: Define o comprimento máximo do código gerado em tokens. Aumente este valor se precisar de códigos mais longos.

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

- Incluir uma visualização prévia do layout XML gerado (para componentes Android)
- Adicionar uma barra de status para mostrar o progresso da geração de código
- Adicionar suporte para mais padrões de design e arquiteturas Android (MVVM, Clean Architecture, etc.)
- Implementar testes unitários e de integração
- Explorar a possibilidade de fine-tuning do modelo para melhorar ainda mais a qualidade do código gerado
- Adicionar suporte para geração de recursos Android (strings, cores, estilos, etc.)

## Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter pull requests ou abrir issues para sugerir melhorias ou reportar bugs.

## Estado Atual do Projeto

O Inovar IADEPG está atualmente em um estado funcional com as seguintes características:

1. Modelo de geração de código que suporta múltiplas linguagens.
2. Suporte específico para desenvolvimento Android, incluindo geração de componentes e layouts XML.
3. Interface de linha de comando (CLI) para interação com o modelo.
4. Interface gráfica do usuário (GUI) para facilitar o uso da ferramenta, incluindo:
   - Capacidade de salvar o código gerado
   - Histórico de códigos gerados com opção de reutilização
   - Opções para personalizar os parâmetros de geração (temperatura, max_length)
5. Documentação atualizada com todas as funcionalidades e instruções de uso.

O projeto está pronto para uso, mas continua em desenvolvimento ativo para melhorias e adição de novas funcionalidades.

