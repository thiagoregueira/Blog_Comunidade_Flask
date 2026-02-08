# 🌐 Comunidade Flask Blog

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

Bem-vindo ao **Comunidade Flask Blog**! Uma plataforma moderna de rede social onde desenvolvedores e entusiastas podem compartilhar conhecimentos, criar conexões e discutir sobre tecnologia. O projeto é construído com Flask e segue as melhores práticas de desenvolvimento web com Python.

## 🚀 Funcionalidades

- **Autenticação Segura**: Login e Cadastro com criptografia de senha (Bcrypt).
- **Perfis de Usuário**: Personalização de perfil com foto, cursos e bio.
- **Feed de Posts**: Criação, edição e exclusão de posts em tempo real.
- **Segurança**: Proteção CSRF, validação de formulários e controle de acesso (@login_required).
- **Design Responsivo**: Interface limpa e adaptável a dispositivos móveis.
- **Povoamento de Dados**: Script automatizado para gerar dados de teste realistas.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Banco de Dados**: SQLAlchemy (SQLite para dev, PostgreSQL para prod)
- **Frontend**: HTML5, CSS3, Bootstrap, Jinja2
- **Formulários**: Flask-WTF
- **Autenticação**: Flask-Login

## 📂 Estrutura do Projeto

```bash
Blog_Comunidade_Flask/
├── comunidade/              # Pacote principal da aplicação
│   ├── static/              # Arquivos estáticos (CSS, Imagens)
│   ├── templates/           # Templates HTML (Jinja2)
│   ├── __init__.py          # Inicialização do App, DB e Configurações
│   ├── forms.py             # Definição de Formulários (Login, Cadastro, Post)
│   ├── models.py            # Modelos do Banco de Dados (Usuario, Post)
│   └── routes.py            # Rotas e Controladores
├── instance/                # Instância do banco de dados (SQLite)
├── .gitignore               # Arquivos ignorados pelo Git
├── create_db.py             # Script auxiliar para criar o banco
├── main.py                  # Ponto de entrada da aplicação
├── povoar_banco.py          # Script para popular o banco com dados de teste
├── Procfile                 # Configuração para deploy (Heroku/Render)
├── README.md                # Documentação do projeto
└── requirements.txt         # Dependências do projeto
```

## ⚡ Começando

Siga as instruções abaixo para configurar o projeto em sua máquina local.

### Pré-requisitos

- Python 3.10 ou superior
- Pip (Gerenciador de pacotes do Python)

### Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/Blog_Comunidade_Flask.git
   cd Blog_Comunidade_Flask
   ```

2. **Crie e ative um ambiente virtual**
   ```bash
   # Windows
   python -m venv .venv
   .\.venv\Scripts\activate

   # Linux/macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare o Banco de Dados**
   Execute o script para criar as tabelas e popular o banco com usuários e posts de exemplo:
   ```bash
   python povoar_banco.py
   ```
   > **Nota:** Este script cria usuários fictícios com perfis variados (DevOps, Data Science, Frontend, etc.) para você ver a aplicação cheia de vida!

5. **Execute a Aplicação**
   ```bash
   python main.py
   ```
   Acesse no navegador: `http://localhost:5000`

## 🧪 Credenciais de Teste

Para facilitar seus testes, criamos um usuário padrão com posts e perfil configurado. As credenciais também são exibidas na tela de login.

| Campo | Valor |
|---|---|
| **Email** | `usuarioteste@email.com` |
| **Senha** | `123456` |

> Você também pode criar sua própria conta clicando em "Criar Conta" na página de login.

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Se você tem alguma ideia para melhorar o projeto:

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/IncrivelFeature`)
3. Faça o Commit de suas mudanças (`git commit -m 'Adiciona a IncrivelFeature'`)
4. Faça o Push para a Branch (`git push origin feature/IncrivelFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido com 💙 por [Thiago Regueira](https://github.com/thiagoregueira)
