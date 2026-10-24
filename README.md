# Django-Python

Backend em Django REST Framework para gerenciar categorias e produtos em um banco SQLite3.

>!Atenção: Caso queira testar pelo link do git pages, primeiro você deve abrir o server local para a API puxar os dados da database. Caso contrário, o site nem abrirá.

## Django

- Site oficial: [www.djangoproject.com](https://www.djangoproject.com/)
- Documentação oficial: [docs.djangoproject.com](https://docs.djangoproject.com/)

## Screenshots da API REST Web [index.html](index.html)

### Home

![Home](/_assets/screenshot1.png)

### Produtos

![Produtos](/_assets/screenshot2.png)

### Categorias

![Categorias](/_assets/screenshot3.png)

## Instalar o ambiente

Abra o **CMD** na pasta raiz do projeto e execute:

```bat
cd djangoAPI
py --version
py -m venv venv
venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\python.exe -m pip install -r requirements.txt
venv\Scripts\python.exe manage.py migrate
```

Esses comandos criam o ambiente virtual do Python e instalam o Django e o Django REST Framework nas versões definidas em `requirements.txt`. O ambiente virtual mantém as dependências deste projeto separadas das demais instalações de Python do computador.

## Iniciar o servidor

Na pasta `djangoAPI`, execute:

```bat
venv\Scripts\python.exe manage.py runserver
```

Deixe o CMD aberto. O servidor estará em `http://127.0.0.1:8000`. Encerre com `Ctrl+C`.

O Django serve as páginas HTML e os arquivos CSS/JavaScript. O JavaScript chama as rotas da API na mesma origem:

- `http://127.0.0.1:8000/` — página inicial.
- `http://127.0.0.1:8000/produtos/` — cadastro, busca e tabela de produtos.
- `http://127.0.0.1:8000/categorias/` — cadastro, busca e tabela de categorias.

Use o endereço `http://127.0.0.1:8000` para acessar o sistema. Não abra os HTML pelo Live Server, pois o Django precisa servir as páginas e a API na mesma origem.

## Como testar o sistema

### 1. Iniciar o backend

Abra um CMD na pasta raiz do projeto e inicie o servidor:

```bat
cd djangoAPI
venv\Scripts\python.exe manage.py runserver
```

Deixe essa janela aberta. Quando aparecer `Starting development server`, o Django está rodando. Acesse pelo navegador:

- `http://127.0.0.1:8000/` — página inicial.
- `http://127.0.0.1:8000/produtos/` — página de produtos.
- `http://127.0.0.1:8000/categorias/` — página de categorias.

Não abra os arquivos HTML diretamente nem use o Live Server: as páginas precisam ser servidas pelo Django para que os templates e as chamadas da API funcionem corretamente.

### 2. Testar pelo site

Na página de categorias, cadastre uma categoria e confirme que ela aparece na tabela. Depois, teste **Editar**, **Buscar** pelo ID ou nome e **Excluir**.

Na página de produtos, cadastre um produto selecionando a categoria criada. Confirme que aparece na tabela com a categoria correta. Depois, teste **Editar**, **Buscar** pelo ID ou nome e **Excluir**.

O campo de busca filtra os registros que já foram carregados na página. Para conferir problemas, abra as ferramentas do navegador com `F12` e veja as abas **Console** e **Network** durante uma ação.

### 3. Testar as rotas da API

Com o servidor ainda aberto, use o navegador para conferir as listagens:

- `http://127.0.0.1:8000/categorias/listar`
- `http://127.0.0.1:8000/produtos/listar`

Para testar cadastro, atualização e exclusão, use o Insomnia. Configure o endereço base `http://127.0.0.1:8000`, escolha o método HTTP indicado na tabela de [rotas](#rotas), e selecione **JSON** no corpo da requisição. Siga esta ordem:

1. Envie um `POST` para `/categorias/cadastrar` com o JSON de cadastro de categoria abaixo. A resposta deve confirmar a criação e trazer o ID.
2. Envie um `POST` para `/produtos/cadastrar` com o JSON de cadastro de produto. Use em `categoria_id` o ID da categoria criada.
3. Use `GET` em `/categorias/buscar/{id}` e `/produtos/buscar/{id}`, substituindo `{id}` pelos IDs retornados, para conferir os registros.
4. Use `PATCH` nas rotas de atualização e confira as alterações com outro `GET`.
5. Use `DELETE` nas rotas de exclusão. Confira que os registros não aparecem mais nas rotas de listagem.

Os exemplos de JSON para cadastro e atualização estão na seção [rotas](#rotas). Para excluir uma categoria, exclua antes os produtos associados a ela.

### 4. Rodar as verificações automatizadas

Abra outro CMD na raiz do projeto. O servidor pode continuar rodando na primeira janela. Execute:

```bat
cd djangoAPI
venv\Scripts\python.exe manage.py check
venv\Scripts\python.exe manage.py test src.rest_api
```

O primeiro comando verifica a configuração do Django. O segundo roda os 10 testes das rotas da API; ao passar, o resultado termina com `OK`. Os testes usam um banco temporário, sem alterar os dados de `djangoAPI\db.sqlite3`.

Para encerrar o servidor, volte à primeira janela do CMD e pressione `Ctrl+C`.

## Banco de dados

O banco é `djangoAPI\db.sqlite3`. As tabelas do projeto são `categorias` (`id`, `nome`) e `produtos` (`id`, `nome`, `preco`, `categoria_id`). Cada produto precisa pertencer a uma categoria existente.

Para visualizar o banco e consultar as tabelas pelo VS Code, você pode instalar a extensão [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer) e abrir o arquivo `djangoAPI\db.sqlite3`.

### Popular com dados de teste

O arquivo `djangoAPI\seed.py` cria 5 categorias e 5 produtos de exemplo. **Atenção:** toda vez que executar o seed, ele apaga todas as categorias e todos os produtos que já estão no banco antes de criar os dados de teste.

No CMD, a partir da pasta raiz do projeto, execute:

```bat
cd djangoAPI
venv\Scripts\python.exe seed.py
```

Ao concluir, a mensagem `5 categorias e 5 produtos de teste cadastrados.` confirma a execução. Abra `http://127.0.0.1:8000/categorias/` e `http://127.0.0.1:8000/produtos/` para visualizar os dados.

Se alterar os modelos em `src\django_db.py`, crie e aplique uma migration:

```bat
cd djangoAPI
venv\Scripts\python.exe manage.py makemigrations core --name nome_da_alteracao
venv\Scripts\python.exe manage.py migrate
```

## Rotas

Use `http://127.0.0.1:8000` como endereço base. As rotas não têm prefixo `/api` nem barra final. Troque `{id}` pelo ID do registro.

| Ação | Categorias | Produtos |
| --- | --- | --- |
| Listar | `GET /categorias/listar` | `GET /produtos/listar` |
| Buscar por ID | `GET /categorias/buscar/{id}` | `GET /produtos/buscar/{id}` |
| Cadastrar | `POST /categorias/cadastrar` | `POST /produtos/cadastrar` |
| Atualizar | `PUT` ou `PATCH /categorias/atualizar/{id}` | `PUT` ou `PATCH /produtos/atualizar/{id}` |
| Excluir | `DELETE /categorias/excluir/{id}` | `DELETE /produtos/excluir/{id}` |

Envie os exemplos abaixo como JSON no Insomnia.

### Categoria

Cadastro — `POST /categorias/cadastrar`:

```json
{
  "nome": "Eletrônicos"
}
```

Atualização — `PATCH /categorias/atualizar/{id}`:

```json
{
  "nome": "Informática"
}
```

### Produto

Cadastro — `POST /produtos/cadastrar` (use um `categoria_id` que exista):

```json
{
  "nome": "Teclado",
  "preco": "120.00",
  "categoria_id": 1
}
```

Atualização — `PATCH /produtos/atualizar/{id}`:

```json
{
  "preco": "99.90"
}
```
