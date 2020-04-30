# Morais Parking
## Estrutura de dados - UNIESP
### Sistema de controle de estacionamento
Projeto referente a segunda nota da matéria de Estrutura de dados

#### Integrantes

1. Antônio Marcos de Macêdo Cavalcanti - marcos.c1337@gmail.com
2. Igor Felipe Sales - igorsales.academico@gmail.com
3. Rodrigo Henrique Soares de Oliveira Andrade - rodrigo_h_soares@hotmail.com

#### Instalação: 

`git clone https://github.com/igorsales99/morais-parking.git`

#### Crie um Virtual Environment
##### Linux
```
$ cd morais-parking
$ python3 -m venv ./venv  //utilize o comando referente ao python 3+
$ source venv/bin/activate 
$ pip install -r requirements.txt
```
##### Windows

```
$cd morais-parking/venv/Scripts
$ activate.bat
```
retorne para o diretório raiz do projeto
```
$ pip install -r requirements.txt
```

#### Executar as migrações django

```$ python manage.py makemigrations
$ python manage.py migrate
```

#### Iniciar Server
`$ python manage.py runserver`
