# Inovar IADEPG

Este projeto tem como objetivo criar uma IA capaz de gerar códigos e programas em várias linguagens, com foco especial em desenvolvimento Android, incluindo geração de código Kotlin e layouts XML.

## Estado Atual do Projeto

O Inovar IADEPG está atualmente em um estado funcional e avançado, pronto para ser implantado no Heroku como uma aplicação web.

## Funcionalidades

- Geração de código em Python, Java, JavaScript, Kotlin e XML
- Interface web para interação com o modelo de geração de código
- Suporte para componentes Android (Activity, Fragment, Service, BroadcastReceiver)
- Interface de linha de comando (CLI) para interação rápida com o modelo
- Interface gráfica do usuário (GUI) robusta

## Estrutura do Projeto

- `code_generation_model.py`: Contém o modelo de geração de código
- `cli.py`: Interface de linha de comando
- `gui.py`: Interface gráfica do usuário
- `app.py`: Aplicação web Flask para implantação no Heroku

## Como usar

### Interface Web (Heroku)

1. Acesse a URL do aplicativo Heroku (após a implantação)
2. Use a interface web para selecionar a linguagem, inserir o prompt e gerar código

### Interface Gráfica (GUI)

1. Instale as dependências: `pip install -r requirements.txt`
2. Execute: `python gui.py`
3. Use a interface para selecionar opções, gerar código e visualizar resultados

### Interface de Linha de Comando (CLI)

Execute comandos como:
```
python cli.py --language python --prompt "def fibonacci(n):"
python cli.py --language kotlin --android activity
python cli.py --language xml --android-layout activity
```

## Como implantar no Heroku

1. Certifique-se de ter uma conta no Heroku e o Heroku CLI instalado
2. Crie um novo aplicativo Heroku usando o painel de controle do Heroku ou o Heroku CLI
3. Configure as variáveis de ambiente necessárias no painel de controle do Heroku
4. Implante o código no Heroku usando git ou o Heroku CLI
5. Abra o aplicativo no navegador usando a URL fornecida pelo Heroku

## Próximos Passos

1. Melhorar a interface do usuário da aplicação web
2. Implementar testes automatizados
3. Adicionar suporte para mais padrões de design e arquiteturas Android (MVVM, Clean Architecture, Jetpack Compose)
4. Explorar fine-tuning do modelo com um dataset de código Android de alta qualidade

## Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter pull requests ou abrir issues para discutir melhorias e novas funcionalidades.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
