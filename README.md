# API em Python com Flask e MongoDb 🐍

API construida em python para prover todo o backend da aplicação do projeto Neo3.

## ⚡ Instalação

### Pré-requisitos

- [Python ](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/#installation)

> **Nota**: É recomendável o uso de [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

### Iniciando

Antes de tudo, é necessárior fazer o download do repositório.

```bash
$ git clone git@github.com:Neoenergia-3/backend.git
```

Depois, tenha certeza que está dentro do diretório do repositório.

```bash
$ cd <caminho/para/backend>
```

Caso você queira utilizar um ambiente virtual, pode rodar os camandos abaixo:

```bash
# Configura o ambiente virtual no diretório atual
$ python3 -m venv ./ 

# Inicia o ambiente virtual
$ . venv/bin/activate
```

### Configurando
Esta é uma API construida em python, juntamente com flask, por isso é necessário instalar o flask e as outras dependências do projeto.

O que pode ser feito pelo seguinte comando:
```bash
$ pip3 install -r requirements.txt 
```

Para prover todo o sistema de armazenamento de dados esta API ultiliza um banco de dados, chamando [MongoDB](https://docs.mongodb.com/guides/server/install/) 💜.

Portanto é necessário conectar o python ao MongoDB, e para isso você precisa da url de conexão do MongoDB, e depois executar os seguintes comandos:

```bash
# Ainda no diretório da aplicação execute:
$ touch api/config.py
 
# Depois disso pegue o url e execute o seguinte comando:
$ echo MONGO_URI="Cole aqui a url do mongo" > api/config.py
```

> **Nota**: Se você não sabe como conseguir o url de conexão do MongoDB da uma olhada [nesse site](https://docs.mongodb.com/guides/server/drivers/).

Pronto! Agora o projeto já está configurado e pronto para uso. 

### 💻 Rodando 
Agora que o projeto ja está configurado e pronto para uso só precisa colocar para rodar.

E para isso basta rodar o seguinte comando:

```bash
# No diretório da aplicação execute:
$ python3 server.py     
```

> **Nota:** Se estiver usando um ambiente virtual, execute este comando dentro dele.


