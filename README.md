# Inovar IADEPG

Este projeto tem como objetivo criar uma IA capaz de gerar códigos e programas em várias linguagens, com foco especial em desenvolvimento Android, incluindo geração de código Kotlin e layouts XML.

## Estado Atual do Projeto

O Inovar IADEPG está atualmente implantado no Heroku como uma aplicação web funcional.

## Funcionalidades

- Geração de código em Python, Java, JavaScript, Kotlin e XML
- Interface web para interação com o modelo de geração de código
- Suporte para componentes Android (Activity, Fragment, Service, BroadcastReceiver)
- Otimização de recursos para melhor desempenho no Heroku

## Como usar

Acesse a aplicação em: https://inovar-iadepg-d32ba9c0af45.herokuapp.com/

1. Selecione a linguagem desejada no menu suspenso.
2. Digite o prompt para a geração de código na caixa de texto.
3. Clique em "Gerar Código" para obter o resultado.

## Estrutura do Projeto

- `app.py`: Aplicação Flask principal
- `code_generation_model.py`: Modelo de geração de código otimizado
- `requirements.txt`: Dependências do projeto
- `runtime.txt`: Versão do Python especificada para o Heroku

## Próximos Passos

1. Implementar testes automatizados
2. Melhorar a qualidade e diversidade do código gerado
3. Adicionar suporte para mais padrões de design e arquiteturas Android
4. Implementar um sistema de feedback para melhorar continuamente o modelo

## Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter pull requests ou abrir issues para discutir melhorias e novas funcionalidades.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
