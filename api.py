from fastapi import FastAPI
from json import JSONDecoder
from subprocess import run

class Api:
    app = FastAPI()
    
    produtos = {
        1:{'produto':'relógio','preço':3000},
        2:{'produto':'celular','preço':1300},
        3:{'produto':'notebook','preço':4000}
    } 

    id = 3

    def __init__(sf) -> None:
        get = sf.app.get
        post = sf.app.post
        put = sf.app.put
        delete = sf.app.delete
        
        @get('/')
        async def home():
            return {'produtos':sf.produtos,'total de produtos':len(sf.produtos)}

        @get('/vendas/{id}/')
        async def obter(id:int): return sf.produtos[id] if id in sf.produtos else {'Erro':'Id inexistente'}

        @post('/')
        async def novo(produto:str):
            try:
                produto = JSONDecoder().decode(produto.replace("'",'"'))
                if not (produto and produto['produto'] and produto['preço']): 
                    return {'Erro':'Informações nulas recusadas'}
                produto['preço'] = float(produto['preço'])
                
                for i in sf.produtos:
                    if produto['produto'] == sf.produtos[i]['produto']: return {'Erro':'Produto repetido'}
            except: return {'Erro':'Valores inválidos'}
            sf.id += 1
            sf.produtos.update({sf.id:{'produto':produto['produto'],'preço':produto['preço']}})
            return {sf.id:sf.produtos[sf.id],'status':'sucesso'}
     
        @post('/vendas/{id}/')
        async def inserir(id:int,produto:str):
            try:
                if id < 1: return {'Erro':'Id inválido'}
                if id in sf.produtos: return {'Erro':'Id repetido'}

                produto = JSONDecoder().decode(produto.replace("'",'"'))
                if not (produto and produto['produto'] and produto['preço']): 
                    return {'Erro':'Informações nulas recusadas'}
                produto['preço'] = float(produto['preço'])

                for i in sf.produtos:
                    if produto['produto'] == sf.produtos[i]['produto']: return {'Erro':'Produto repetido'}
            except: return {'Erro':'Valores inválidos'}

            sf.produtos.update({id:{'produto':produto['produto'],'preço':produto['preço']}})
            return {id:sf.produtos[id],'status':'sucesso'}

        @put('/vendas/{id}/')
        async def alterar(id:int,atributos:str):
            if not id in sf.produtos: return {'Erro':'Id inexistente'}
            try:
                atributos = JSONDecoder().decode(atributos.replace("'",'"'))
                if 'produto' in atributos: sf.produtos[id]['produto'] = atributos['produto']
                if 'preço' in atributos: sf.produtos[id]['preço'] = float(atributos['preço'])
            except: return {'Erro':'Valores inválidos'}
            return {id:sf.produtos[id],'status':'Alterado com sucesso'}
        
        @delete('/vendas/{id}/')
        async def deletar(id:int):
            if not id in sf.produtos: return {'Erro':'Id inexistente'}
            deletado = sf.produtos.pop(id)
            return {id:deletado,'status':'Deletado com sucesso'}

app = Api().app

if __name__=='__main__':
    print('Iniciou')
    try: process = run(['uvicorn','api:app','--reload'], capture_output=True, text=True)
    except KeyboardInterrupt:...