from browser import document
import time

import json
import ast
import datetime


identar = True #@param {type:"boolean"}
espacos_identacao = 4 #@param {type:"integer"}
ordenar = False #@param {type:"boolean"}
somente_ascii = False #@param {type:"boolean"}
dicionario = "{'result': {'country': {'long_name': 'Brasil', 'short_name': 'BR'}, 'state': {'long_name': 'São Paulo', 'short_name': 'SP'}, 'city': {'long_name': 'Ribeirão Preto', 'short_name': 'Ribeirão Preto'}, 'district': None, 'neighborhood': {'long_name': 'Distrito de Bonfim Paulista', 'short_name': 'Distrito de Bonfim Paulista'}, 'street': {'long_name': '9', 'short_name': '9'}, 'slug': '9-distrito-de-bonfim-paulista-ribeirao-preto-sp-brasil', 'geometry': {'location': {'lat': -21.2345726, 'lng': -47.8181069}, 'viewport': {'northeast': {'lat': -21.2332236197085, 'lng': -47.81675791970851}, 'southwest': {'lat': -21.23592158029151, 'lng': -47.81945588029151}}}}}" #@param {type:"string"}
dicionario = eval(dicionario)

if identar:
  app_json = json.dumps(
      dicionario,
      indent=espacos_identacao,
      ensure_ascii=somente_ascii,
      sort_keys=ordenar,
      default=str
  )
else:
  app_json = json.dumps(dicionario, default=str)
# print(app_json)
document['dict-textarea'].text = dicionario
document['json-textarea'].text = app_json



# title = 'Python'
# document['header'].html = f"Hello, {title}!"

# counter = 0

# def increment(ev):
#     global counter
#     counter += 1
#     document['counter'].html = str(counter)

# document["counter-button"].bind("click", increment)

# # check console
# current_time = int(time.strftime('%H'))
# if current_time < 12 :
#       print('Good morning')
#       document['cumprimento'].html = 'Good morning'
# elif 12 <= current_time < 18:
#       print('Good afternoon')
#       document['cumprimento'].html = 'Good afternoon'
# else:
#       print('Good evening')
#       document['cumprimento'].html = 'Good evening'
