# Desafio Orama


API rest recebe requisição POST conforme **"/exemplo/freelancer.json"** computa o total de meses que o freelancer trabalhou com cada habilidade e retorna JSON  como **"/exemplo/response.json"**

### Desenvolvido em Python 3.7 utilizando Flask:

** 1. desafio.py **  = fonte do app
** 2. tratajson.py** = tratamento da requisição.

### App Cloud Foundry disponibilizado na IBM Cloud:

Docker customizado com a bibliotecas Python utilizadas:
** 1. Dockerfile ** = configuração do docker
** 2. requirements.txt ** = instalação das bibliotecas
** 3. Procfile ** = chamada do app no docker
** 4. setup.py ** = Setup padrão IBM Cloud Foundry

### DEPLOY:
$ ibmcloud cf push desafiooramanunes

### RODAR TESTE LOCAL:
$ python desafio.py

### URL ACESSO PÚBLICO:
https://desafiooramanunes.mybluemix.net/freelancer

OBS: foi feito na conta free da IBM com 2000 requisições mensais somente. após este limite para de responder.
