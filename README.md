
# Mutualizo API

Projeto de API feito com o propósito de teste, que realiza diferentes tarefas de acordo com o endpoint chamado, o projeto em questão utiliza Docker para baixar as dependências da aplicação, criar uma imagem da mesma e subir o servidor através do docker-compose.

Antes de prosseguir, certifique-se de que o [Docker Desktop](https://www.docker.com/products/docker-desktop/) esteja instalado na sua máquina local. O Docker Desktop precisa estar ativo no momento do teste, para que o passo a passo abaixo seja eficaz.
## Sumário

- [Rodando localmente](#Rodando-localmente)
- [Documentação das rotas da API](#Documentação-das-rotas-da-API)
- [Autenticação e autorização](#Autenticação-e-autorização)
- [Rotas existentes](#Rotas-existentes)
- [Rodando os testes](#Rodando-os-testes)
- [Ferramentas utilizadas](#Ferramentas-utilizadas)
- [Referências](#Referências)


## Rodando localmente

### Abra o terminal do seu editor de códigos e clone o projeto

```powershell
  git clone https://github.com/gabrielsimplicio00/mutualizo.git
```

### Entre no diretório do projeto

```powershell
  cd mutualizo
```

### Crie a imagem docker da API

Essa imagem vai servir como base para subir o container da aplicação com o Docker Compose.

```powershell
  docker build -t mutualizo-api .
```

Esse comando executará uma série de tarefas descritas no Dockerfile, criando uma imagem personalizada que tem como base a imagem oficial do Python no [Docker Hub](https://hub.docker.com/) e instalando todas as dependências necessárias para o projeto, que estão na pasta requirements.txt.

### Inicialize o container com o docker compose, que terá como base a imagem recém criada

```powershell
  docker compose up
```

Esse comando irá usar as informações do arquivo docker-compose.yml para subir os serviços necessários ao funcionamento da API, bem como iniciar um servidor local a partir da dependência uvicorn.

Para desativar o servidor local, utilize o comando Ctrl+C.

## Documentação das rotas da API

Em seu computador, a URL padrão de acesso é:

```http
  http://localhost:8000
```

Porém, existem outras alternativas para testar as funcionalidades de forma mais prática.

## Documentação automática do FastAPI

Para fazer as requisições de forma mais prática, o FastAPI já vem com uma rota embutida, que redireciona a API para uma interface Swagger, nessa rota é possível testar todas as funcionalidades de forma prática.

```http
  http://localhost:8000/docs
```

## Autenticação e autorização

Antes de testar as rotas, é necessário falar sobre a segurança da API. Um banco de dados fake foi utilizado para simular a existência de usuários previamente cadastrados. A partir de um nome de usuário e senha, a autorização para acessar as rotas é concedida. Os dados dos usuários podem ser encontrados em __src/users.py__.

Existem, no total, 2 usuários no banco. Um deles está habilitado para fazer login, já o outro se encontra desabilitado. Tentar efetuar o login com o usuário desabilitado levará em erro.

Dados do usuário habilitado:

```
    username: "userteste"
    password: "secret"
```

Ao acessar a documentação automática do FastAPI em __http://localhost:8000/docs__, haverá um botão "Authorize" no canto direito. Ao clicar no botão e inserir os dados do usuário você estará autorizado a acessar os endpoints (os campos abaixo de username e password não precisam ser preenchidos).

Caso haja tentativa de acesso aos endpoints sem autorização prévia, uma resposta HTTP de código 401 _(Unauthorized)_ será lançada.

A API em questão utiliza OAuth2 como meio de autenticação, caso queira efetuar os testes em um programa próprio (Postman ou Insomnia), o token de autorização é __Bearer userteste__.

## Rotas existentes

As query strings são essenciais para fornecimento dos parâmetros para as funções que vão ser chamadas. Dito isso, vamos às rotas existentes.

### Retorna o número fornecido de forma invertida

Exemplo:

```http
  GET /reverse_integers?integer=-123
```

```
  {
    "resultado": "-321"
  }
```

| Query   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `integer`      | `int` | **Obrigatório**. O número que será invertido |

### Retorna o comprimento médio das palavras de uma frase

Exemplo:

```http
  GET /average_words_length?sentence=Hi all, my name is Tom...I am originally from Brazil.
```

```
  {
    "resultado": 3.55
  }
```

| Query   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `sentence`      | `string` | **Obrigatório**. A frase que servirá para o cálculo |

### Retorna duas listas de palavras de acordo com as duas frases fornecidas

Exemplo
```http
  GET /matched_mismatched_words?sentence1=We are really pleased to meet you in our city&sentence2=The city was hit by a really heavy storm
```

Nesse caso, duas listas aparecerão no resultado, a primeira será de palavras que não são comuns entre as duas frases, a última será de palavras em comum entre elas.

```
  {
  "resultado": [
    [
      "meet",
      "We",
      "pleased",
      "hit",
      "by",
      "in",
      "The",
      "our",
      "to",
      "heavy",
      "you",
      "are",
      "storm",
      "a",
      "was"
    ],
    [
      "city",
      "really"
    ]
  ]
}
```

| Query   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `sentence1`      | `string` | **Obrigatório**. A primeira frase |
| `sentence2`      | `string` | **Obrigatório**. A segunda frase |


## Rodando os testes

Para rodar todos os testes unitários a partir da raíz do projeto, abra outro terminal e escreva o seguinte comando:

```powershell
  # em ./mutualizo
  pytest src/test_main.py
```
## Ferramentas utilizadas

**Back-end:** Python, FastAPI, Docker


## Referências

 - [Documentação do FastAPI](https://fastapi.tiangolo.com/)
 - [Documentação do Docker](https://docs.docker.com/)
 - [Documentação do Python](https://docs.python.org/pt-br/3/)

