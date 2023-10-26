from fastapi import FastAPI
from pydantic import BaseModel #cria um modelo de dados

#criando modelo de dados
class ProdutoCriar(BaseModel):
    codigo: int
    nome: str
    qtd: int
    preco: float


app= FastAPI()

produtos = [
    {
        'codigo':1,
        'nome': 'violão',
        'qtd':12,
        'preco':500
    }
]

@app.get('/')
def raiz():
    return 'Olá mundo!!!'

@app.get('/produtos')
def listagem_de_produtos():
    return produtos

@app.get('/produtos/{codigo}')
def listar_produto_por_codigo(codigo):
    for i in produtos:
        if i['codigo'] == codigo:
            return i
    return 'Produto não encontrado'

@app.get('/usuarios')
def listagem_de_usuarios():
    return ('Aqui serão listados os usuários')
#crie uma rota que retorna a frase 'lista de usuarios'

@app.post('/produtos')
def criar_produtos(dados: ProdutoCriar):
    produtos.append(
        {
            'codigo': dados.codigo,
            'nome': dados.nome,
            'qtd': dados.qtd,
            'preco': dados.preco
        }
    )
    return 'produto criado'
