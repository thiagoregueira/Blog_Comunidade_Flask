from comunidade import app, database
from comunidade.models import Usuario
import urllib.request
import os


def atualizar_avatares():
    with app.app_context():
        # Lista dos usuários de teste que devem receber avatares
        usuarios_teste = [
            'Lira',
            'Joao',
            'Alon',
            'Ana_Souza',
            'Dev_Bruno',
            'Carla_Front',
            'Daniel_Backend',
            'Elena_UX',
            'Fabio_Sec',
            'Gabi_Mobile',
            'Hugo_Cloud',
            'Isa_PM',
            'Jorge_AI',
            'usuarioteste',
        ]

        # Filtrar apenas os usuários de teste
        usuarios = Usuario.query.filter(Usuario.username.in_(usuarios_teste)).all()

        if not os.path.exists('comunidade/static/fotos_perfil'):
            os.makedirs('comunidade/static/fotos_perfil')

        print(f'Encontrados {len(usuarios)} usuários de teste para atualizar fotos de perfil...')

        for usuario in usuarios:
            # Usar o estilo 'adventurer' do DiceBear que lembra animes/RPG
            # Adicionamos flip=true para variar
            url = f'https://api.dicebear.com/9.x/adventurer/png?seed={usuario.username}&backgroundColor=b6e3f4,c0aede,d1d4f9,ffdfbf,ffd5dc&radius=50'

            nome_arquivo = f'{usuario.username}_anime.png'
            caminho_arquivo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arquivo)

            if not os.path.exists(caminho_arquivo):
                try:
                    # Baixar a imagem
                    print(f'Baixando avatar para {usuario.username}...')
                    urllib.request.urlretrieve(url, caminho_arquivo)

                    # Atualizar no banco
                    usuario.foto_perfil = nome_arquivo
                    print(f'Avatar atualizado para {usuario.username}')

                except Exception as e:
                    print(f'Erro ao atualizar avatar de {usuario.username}: {e}')
            else:
                print(f'Avatar de {usuario.username} já existe.')
                # Garantir que o banco aponte para o arquivo correto mesmo se já existir
                if usuario.foto_perfil != nome_arquivo:
                    usuario.foto_perfil = nome_arquivo
                    print(f'Link do avatar atualizado no banco para {usuario.username}')

        database.session.commit()
        print('Todos os avatares foram atualizados com sucesso!')


if __name__ == '__main__':
    atualizar_avatares()
