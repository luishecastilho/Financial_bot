# proprio\_\_bot-deriv

1- cria ambiente virtual
python3 -v venv venv

2- instala as dependencias no ambiente virtual
source venv/bin/activate
pip install django pillow

3- inicia o projeto
mkdir 'nome'
cd 'nome'
django-admin startproject NOMEDOPROJTO .

4- cria parte do projeto
python3 manage.py startapp PARTEDOPROJETO (cria um segmento do projeto, tipo 'produtos/)

5- start localserver
python3 manage.py runserver

ESSA FUNÇÃO DO DERIV SER UMA CLASSE
para a conexão já estar pronta e dps só pegar os dados

quando por em produção, precisa rodar esse comando para ele coletar todos os arquivos estáticos
python3 manage.py collectstatic



ATUALIZA banco
python3 manage.py makemigrations

SALVA atualização do banco
python3 manage.py migrate