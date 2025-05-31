
# 🔐 JWT e Segurança em Python

Este projeto tem como finalidade demonstrar a implementação de autenticação utilizando tokens JWT em aplicações Python, com o uso do framework Flask e seguindo a arquitetura MVC.

O desenvolvimento foi realizado em paralelo ao curso "Autenticação JWT e Segurança", promovido pela Rocketseat. Durante o processo, foram adquiridos conhecimentos sobre boas práticas na estruturação de aplicações backend, proteção de rotas por meio de tokenização, além de um entendimento aprofundado sobre o funcionamento interno da criptografia dos tokens JWT.

Neste projeto, é simulado um sistema bancário no qual é possível realizar a criação de um usuário, efetuar login e, posteriormente, editar o saldo bancário desse usuário. A edição do saldo só é permitida mediante a validação adequada do token JWT, garantindo a segurança da operação.

## ⚙️ Rodando localmente

#### 1. Clone o projeto


```bash
  git clone https://github.com/LucasVizoto/jwt-python
```
#### 2. Crie e ative um ambiente virtual


```bash
python -m venv venv

source venv/bin/activate   # Linux/MacOS
venv\Scripts\activate      # Windows

```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4. Configure as variáveis de ambiente

Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

```bash
KEY=<sua-chave-secreta>
ALGORITHM=<algoritmo-utilizado>
JWT_HOURS=<duração-do-token-em-horas>

```

#### 5. Inicie o Servidor

```
  python run.py
```


## 📖 Documentação da API

- Criar um novo Usuário

```http
  POST /bank/registry
```

#### Body da Requisição:
| Campo   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Obrigatório**. Nome de usuário para login. |
`password` | `string`| **Obrigatório**. Senha que será encriptada.

#### Resposta esperada: 
```http
{
    "data": {
        "count": int,
        "type": "User",
        "username": "exemplo"
        }
}

```
---
####

- Login e geração do token JWT

```http
  POST /bank/login
```
#### Body da Requisição:
| Campo   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Obrigatório**. Nome de usuário para login. |
`password` | `string`| **Obrigatório**. Senha que será encriptada.

#### Resposta esperada: 
```http
{
    "data": {
        "access": true,
        "auth": "seu_token_jwt",
        "username": "exemplo"
        }
}

```

---
#### 
- Atualização de saldo do usuário

```http
  PATCH /bank/balance/<user_id>
```
#### Body da Requisição:
| Request   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `new_balance`      | `float` | **Obrigatório**. Valor que será atualizado no banco.|

#### Autenticação e Cabeçalhos Necessários

####    🔐 Autenticação: Esta rota requer um Bearer Token no cabeçalho Authorization, utilizando o token obtido na rota de login.

####    🧾 Cabeçalhos adicionais:
- ``uid``: Deve conter o ID do usuário correspondente, inserido no cabeçalho Headers.

- ``user_id``: Deve ser passado também nos parâmetros da URL (Params) e deve ser igual ao ID do usuário que se deseja alterar.

#### ⚠️ Certifique-se de que os valores de uid no cabeçalho e user_id na URL correspondam ao mesmo usuário. Caso contrário, a requisição será rejeitada por motivos de segurança.

#### Resposta esperada: 
```http
{
    "data": {
        "count": int,
        "new_balance": exemplo.float,
        "type": "User"
        }
}

```



## 🔗Links

 - [Link para o curso](https://app.rocketseat.com.br/classroom/autenticacao-jwt-e-seguranca)
 - [Certificado](https://app.rocketseat.com.br/certificates/393fdcd8-ad4c-4c88-b9be-32d78b3551fb)


## 🔎 Onde me encontrar

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lucasvizoto/)

[![e-mail](https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white)](mailto:lucavizoto364@gmail.com)
