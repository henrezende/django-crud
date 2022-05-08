# CRUD Alunos

## Requisitos de sistema

- Docker

## Rodando a aplicação

- Inicie o container em modo desacoplado: `docker-compose up -d --build`
- Rode as migrations: `docker-compose run web python manage.py migrate`
- Acesse a documentação da API em `http://localhost:8000/swagger/`

### Rodando os tests

- Para rodar a suite completa de testes: `docker-compose run web python manage.py test`
- Para rodar teste em um arquivo específico: `docker-compose run web python manage.py test students.tests`.

### Rodando o code analyzer (linter)

- Apenas rode o comando `docker-compose run web pylint --rcfile=.pylintrc *` e as alterações necessárias serão apontadas

### Rodando migrations

- Rode `docker-compose run web python manage.py migrate_schemas`

### Rodando os comandos diretamente dentro do container

- Primeiro entre no bash `docker-compose run web bash`
- Então rode os comandos descritos acima sem `docker-compose run web` no início, ex: `python manage.py test` ao invés de `docker-compose run web python manage.py test`
