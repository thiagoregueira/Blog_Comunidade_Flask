from comunidade import app, database, bcrypt
from comunidade.models import Usuario, Post


def povoar_banco():
    with app.app_context():
        # Dados fictícios para popular o banco
        usuarios_ficticios = [
            {
                'username': 'Lira',
                'email': 'lira@email.com',
                'password': '123',
                'cursos': 'Excel;VBA;Power BI',
                'posts': [
                    {
                        'titulo': 'Bem-vindo à Comunidade Flask',
                        'corpo': 'Estamos muito felizes em tê-lo aqui! Esta comunidade é para aprendizado e compartilhamento de conhecimento sobre Python e Flask.',
                    },
                    {
                        'titulo': 'Dicas de Excel',
                        'corpo': 'Alguém tem dicas sobre como otimizar planilhas grandes no Excel? Estou tendo problemas com lentidão em alguns arquivos.',
                    },
                ],
            },
            {
                'username': 'Joao',
                'email': 'joao@email.com',
                'password': '123',
                'cursos': 'Python;Ciência de Dados',
                'posts': [
                    {
                        'titulo': 'Análise de Dados com Python',
                        'corpo': 'Acabei de começar o curso de Ciência de Dados e estou adorando a biblioteca Pandas. É incrível como ela facilita a manipulação de dados!',
                    },
                    {
                        'titulo': 'Projeto de Machine Learning',
                        'corpo': 'Estou trabalhando em um projeto de previsão de preços de casas. Alguém já usou o Scikit-learn para isso? Alguma recomendação de algoritmo?',
                    },
                ],
            },
            {
                'username': 'Alon',
                'email': 'alon@email.com',
                'password': '123',
                'cursos': 'SQL;Banco de Dados',
                'posts': [
                    {
                        'titulo': 'Melhores Práticas SQL',
                        'corpo': 'Sempre use índices em colunas que são frequentemente usadas em cláusulas WHERE. Isso melhora muito a performance das consultas.',
                    },
                    {
                        'titulo': 'Flask vs Django',
                        'corpo': 'Qual framework vocês preferem para desenvolvimento web em Python? Flask ou Django? Eu gosto da simplicidade do Flask, mas o Django já vem com muita coisa pronta.',
                    },
                ],
            },
            {
                'username': 'Ana_Souza',
                'email': 'ana.souza@email.com',
                'password': '123',
                'cursos': 'Python;Ciência de Dados;Machine Learning',
                'posts': [
                    {
                        'titulo': 'Visualização de Dados com Seaborn',
                        'corpo': 'Pessoal, recomendo muito explorarem a biblioteca Seaborn para gráficos estatísticos. É muito mais bonita e fácil de usar que o Matplotlib puro!',
                    },
                    {
                        'titulo': 'Carreira em Data Science',
                        'corpo': 'Para quem está começando: foquem em estatística básica antes de pular para modelos complexos de Deep Learning. A base é fundamental.',
                    },
                ],
            },
            {
                'username': 'Dev_Bruno',
                'email': 'bruno.dev@email.com',
                'password': '123',
                'cursos': 'Python;Automação;DevOps',
                'posts': [
                    {
                        'titulo': 'Automatizando tarefas repetitivas',
                        'corpo': 'Hoje consegui automatizar o envio de relatórios semanais com um script Python simples e crontab. Sensação incrível de produtividade!',
                    },
                    {
                        'titulo': 'Docker é vida',
                        'corpo': "Depois que comecei a usar containers para meus ambientes de desenvolvimento, nunca mais tive problemas de 'na minha máquina funciona'.",
                    },
                ],
            },
            {
                'username': 'Carla_Front',
                'email': 'carla.dias@email.com',
                'password': '123',
                'cursos': 'HTML;CSS;JavaScript',
                'posts': [
                    {
                        'titulo': 'Integração Flask + React',
                        'corpo': 'Estou estudando como criar uma API REST com Flask para consumir em um front-end React. Alguém tem tutoriais bons sobre autenticação JWT?',
                    },
                    {
                        'titulo': 'CSS Grid vs Flexbox',
                        'corpo': 'A eterna discussão. Eu pessoalmente acho que Grid é melhor para layouts de página inteira e Flexbox para componentes menores. O que acham?',
                    },
                ],
            },
            {
                'username': 'Daniel_Backend',
                'email': 'daniel.rocha@email.com',
                'password': '123',
                'cursos': 'Python;Flask;Django',
                'posts': [
                    {
                        'titulo': 'Estrutura de pastas no Flask',
                        'corpo': 'Organizar um projeto Flask grande pode ser desafiador. Estou gostando muito do padrão Factory Application e Blueprints.',
                    },
                    {
                        'titulo': 'SQLAlchemy é poderoso demais',
                        'corpo': 'Hoje descobri como fazer consultas complexas com joins e subqueries usando apenas o ORM. A curva de aprendizado vale a pena.',
                    },
                ],
            },
            {
                'username': 'Elena_UX',
                'email': 'elena.costa@email.com',
                'password': '123',
                'cursos': 'Design;UI/UX',
                'posts': [
                    {
                        'titulo': 'Acessibilidade na Web',
                        'corpo': 'Não esqueçam das tags ARIA e do contraste de cores, pessoal! A web deve ser para todos.',
                    },
                    {
                        'titulo': 'Feedback visual em formulários',
                        'corpo': 'É muito importante dar feedback imediato ao usuário quando ele preenche um campo errado. Validar no front e no back é essencial.',
                    },
                ],
            },
            {
                'username': 'Fabio_Sec',
                'email': 'fabio.silva@email.com',
                'password': '123',
                'cursos': 'Segurança da Informação;Python',
                'posts': [
                    {
                        'titulo': 'Cuidado com SQL Injection',
                        'corpo': 'Lembrem-se sempre de parametrizar suas queries ou usar o ORM corretamente. Nunca concatenem strings diretamente no SQL!',
                    },
                    {
                        'titulo': 'Senhas seguras',
                        'corpo': 'O bcrypt que usamos aqui no projeto é ótimo porque já salta a senha automaticamente. Nunca salvem senhas em texto puro.',
                    },
                ],
            },
            {
                'username': 'Gabi_Mobile',
                'email': 'gabriela.mota@email.com',
                'password': '123',
                'cursos': 'Python;Kivy;Flutter',
                'posts': [
                    {
                        'titulo': 'Python no mobile?',
                        'corpo': 'Estou testando o Kivy para criar apps nativos com Python. É interessante, mas a performance ainda não se compara ao Flutter ou Swift.',
                    },
                    {
                        'titulo': 'API First',
                        'corpo': 'Sempre desenhem a API antes de começar a codar o front mobile. Isso evita muito retrabalho depois.',
                    },
                ],
            },
            {
                'username': 'Hugo_Cloud',
                'email': 'hugo.santos@email.com',
                'password': '123',
                'cursos': 'AWS;Azure;Python',
                'posts': [
                    {
                        'titulo': 'Deploy na AWS',
                        'corpo': 'Configurei o EC2 com Nginx e Gunicorn para rodar nossa aplicação Flask. Ficou super estável!',
                    },
                    {
                        'titulo': 'Serverless com Python',
                        'corpo': 'Alguém já brincou com AWS Lambda? Fiz uma função simples para processar imagens e é muito barato e rápido.',
                    },
                ],
            },
            {
                'username': 'Isa_PM',
                'email': 'isabela.ferreira@email.com',
                'password': '123',
                'cursos': 'Gestão Ágil;Scrum',
                'posts': [
                    {
                        'titulo': 'Organização de Backlog',
                        'corpo': 'Manter o backlog limpo e priorizado é a chave para não se perder no desenvolvimento de software.',
                    },
                    {
                        'titulo': 'Dailies produtivas',
                        'corpo': 'Dica rápida: daily meeting tem que ser rápida! O que fiz ontem, o que farei hoje e se tenho impedimentos. Só isso.',
                    },
                ],
            },
            {
                'username': 'Jorge_AI',
                'email': 'jorge.pereira@email.com',
                'password': '123',
                'cursos': 'Inteligência Artificial;Python',
                'posts': [
                    {
                        'titulo': 'LLMs e Chatbots',
                        'corpo': 'Estou integrando a API da OpenAI com Flask para criar um assistente virtual. As possibilidades são infinitas.',
                    },
                    {
                        'titulo': 'Ética em IA',
                        'corpo': 'Precisamos discutir mais sobre viés nos algoritmos de machine learning. Não é só código, é impacto social.',
                    },
                ],
            },
            {
                'username': 'usuarioteste',
                'email': 'usuarioteste@email.com',
                'password': '123456',
                'cursos': 'Python;Flask;Teste',
                'posts': [
                    {
                        'titulo': 'Conta de Teste',
                        'corpo': 'Esta é uma conta de demonstração para novos usuários testarem a aplicação sem precisar se registrar.',
                    },
                    {
                        'titulo': 'Bem-vindo!',
                        'corpo': 'Sinta-se à vontade para explorar, editar perfil e criar novos posts com esta conta.',
                    },
                ],
            },
        ]

        # Iterar sobre os usuários e criar se não existirem
        for usuario_data in usuarios_ficticios:
            usuario_existente = Usuario.query.filter_by(email=usuario_data['email']).first()

            if not usuario_existente:
                senha_criptografada = bcrypt.generate_password_hash(usuario_data['password']).decode('utf-8')
                novo_usuario = Usuario(
                    username=usuario_data['username'],
                    email=usuario_data['email'],
                    password=senha_criptografada,
                    cursos=usuario_data['cursos'],
                )
                database.session.add(novo_usuario)
                database.session.commit()  # Commit para gerar o ID do usuário
                print(f'Usuário {usuario_data["username"]} criado com sucesso!')

                # Criar posts para o novo usuário
                for post_data in usuario_data['posts']:
                    novo_post = Post(titulo=post_data['titulo'], corpo=post_data['corpo'], autor=novo_usuario)
                    database.session.add(novo_post)

                database.session.commit()
                print(f'Posts do usuário {usuario_data["username"]} criados com sucesso!')
            else:
                print(f'Usuário {usuario_data["username"]} já existe no banco de dados.')

    # Executar a atualização dos avatares para estilo anime
    try:
        from atualizar_avatares import atualizar_avatares

        print('-' * 30)
        # print("Iniciando download de avatares personalizados...")
        atualizar_avatares()
    except Exception as e:
        print(f'Erro ao tentar atualizar avatares: {e}')


if __name__ == '__main__':
    povoar_banco()
