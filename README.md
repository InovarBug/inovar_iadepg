# Inovar IADEPG

Este projeto tem como objetivo criar uma IA capaz de gerar códigos e programas em várias linguagens, com foco especial em desenvolvimento Android, incluindo geração de código Kotlin e layouts XML.

## Estado Atual do Projeto

O Inovar IADEPG está atualmente em um estado funcional e avançado com as seguintes características:

1. Modelo de geração de código que suporta múltiplas linguagens (Python, Java, JavaScript, Kotlin, XML).
2. Suporte específico para desenvolvimento Android, incluindo geração de componentes e layouts XML.
3. Interface de linha de comando (CLI) para interação rápida com o modelo.
4. Interface gráfica do usuário (GUI) robusta com as seguintes funcionalidades:
   - Geração de código com opções personalizáveis
   - Capacidade de salvar o código gerado em arquivo
   - Histórico de códigos gerados com opção de reutilização
   - Visualização prévia do layout XML gerado
   - Barra de progresso e rótulo de status para acompanhamento da geração de código
5. Documentação detalhada com instruções de uso e descrição das funcionalidades

## Estrutura do Projeto

- `code_generation_model.py`: Contém o modelo de geração de código.
- `cli.py`: Interface de linha de comando.
- `gui.py`: Interface gráfica do usuário.

## Como usar

### Interface Gráfica (GUI)

1. Instale as dependências: `pip install transformers torch`
2. Execute: `python gui.py`
3. Use a interface para selecionar opções, gerar código e visualizar resultados.

### Interface de Linha de Comando (CLI)

Execute comandos como:
```
python cli.py --language python --prompt "def fibonacci(n):"
python cli.py --language kotlin --android activity
python cli.py --language xml --android-layout activity
```

### Online

O projeto pode ser executado em plataformas como Google Colab, Repl.it ou Binder.

## Funcionalidades de Desenvolvimento Android

- Geração de componentes: Activity, Fragment, Service, BroadcastReceiver
- Geração de layouts XML: Activity, Fragment, item de lista

## Próximos Passos

1. Adicionar suporte para mais padrões de design e arquiteturas Android:
   - Implementar geração de código seguindo o padrão MVVM
   - Adicionar suporte para Clean Architecture
   - Incluir exemplos de uso de Jetpack Compose

2. Implementar testes unitários e de integração:
   - Criar testes para o modelo de geração de código
   - Implementar testes para a CLI e GUI
   - Configurar integração contínua (CI) para execução automática de testes

3. Explorar fine-tuning do modelo:
   - Coletar um dataset de código Android de alta qualidade
   - Realizar fine-tuning do modelo com este dataset
   - Avaliar e comparar a qualidade do código gerado antes e depois do fine-tuning

4. Adicionar suporte para geração de recursos Android:
   - Implementar geração de arquivos de strings (strings.xml)
   - Adicionar suporte para geração de arquivos de cores e estilos
   - Criar templates para outros recursos comuns (drawables, menus, etc.)

5. Melhorar a integração com ferramentas de desenvolvimento Android:
   - Adicionar opção para gerar projetos Android completos
   - Implementar integração com o Android Studio (possivelmente via plugin)

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para submeter pull requests ou abrir issues para sugerir melhorias ou reportar bugs.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

