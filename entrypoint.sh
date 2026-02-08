#!/bin/bash
set -e

# Configurar locale e encoding para UTF-8
export LANG=C.UTF-8
export LC_ALL=C.UTF-8
export PYTHONIOENCODING=utf-8

echo "Iniciando aplicação Blog Comunidade Flask..."
echo "Verificando dependências de banco de dados..."

# Tentar popular o banco com encoding correto
# O script povoar_banco.py já verifica se os usuários existem, então é seguro rodar sempre
echo "Executando script de povoamento (seed)..."
python povoar_banco.py

echo "Iniciando servidor Gunicorn..."
# Gunicorn com 4 workers e timeout generoso, bind na porta 5000
exec gunicorn --bind 0.0.0.0:5000 --workers 4 --timeout 120 main:app
