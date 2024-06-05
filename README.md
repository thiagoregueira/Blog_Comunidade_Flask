# Comunidade

Este é um projeto de uma comunidade online, onde os usuários podem compartilhar seus pensamentos e interagir uns com os outros. O projeto foi desenvolvido usando Flask, um microframework para Python.

## Funcionalidades

- **Autenticação de usuários**: Os usuários podem se registrar e fazer login na plataforma. A autenticação é gerenciada pelo Flask-Login.
- **Perfil de usuário**: Cada usuário tem um perfil onde pode atualizar suas informações pessoais, incluindo uma foto de perfil.
- **Posts**: Os usuários podem criar posts para compartilhar seus pensamentos com a comunidade. Cada post está associado ao usuário que o criou.
- **Contato**: Há uma página de contato onde os usuários podem encontrar informações de contato do desenvolvedor.

## Estrutura do Projeto

O projeto é estruturado da seguinte forma:

- `comunidade/`: Este diretório contém a lógica principal do aplicativo. Ele inclui arquivos para rotas, modelos e formulários.
- `comunidade/models.py`: Este arquivo define os modelos de dados para o aplicativo, incluindo o modelo de usuário e o modelo de post.
- `comunidade/routes.py`: Este arquivo define as rotas para o aplicativo.
- `comunidade/forms.py`: Este arquivo define os formulários usados no aplicativo.
- `comunidade/templates/`: Este diretório contém os templates HTML usados para renderizar as páginas do aplicativo.
- `comunidade/static/`: Este diretório contém arquivos estáticos, como CSS e imagens.
- `create_db.py`: Este script cria o banco de dados para o aplicativo.
- `main.py`: Este é o ponto de entrada para o aplicativo.

## Produção

O projeto está atualmente em produção e pode ser acessado em https://comunidade-pensar.glitch.me/

## Como executar localmente

Para executar o projeto localmente, siga estas etapas:

1. Clone o repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Execute `python create_db.py` para criar o banco de dados.
4. Execute `python main.py` para iniciar o aplicativo.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
