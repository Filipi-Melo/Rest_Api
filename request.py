from requests import get,post,put,delete

# Documentação detalhada da api: http://127.0.0.1:8000/docs

#Get
print(get('http://127.0.0.1:8000/vendas/1').json())
print(get('http://127.0.0.1:8000/vendas/2').json())
print(get('http://127.0.0.1:8000/vendas/3').json(),'\n')

#Post
print(post('http://127.0.0.1:8000/?produto={"produto":"rolex","preço":10000}').json(),'\n')
print(post('http://127.0.0.1:8000/vendas/10/?produto={"produto":"colar","preço":80}').json(),'\n')

#Put
print(put('http://127.0.0.1:8000/vendas/2/?atributos={"produto":"carro","preço":120000}').json(),'\n')

#Delete
print(delete('http://127.0.0.1:8000/vendas/3/').json(),'\n')

print('Todos os produtos:\n',get('http://127.0.0.1:8000').json())