from browser import bind, document, alert
import time

import json
import ast
import datetime

@bind("#button3", "click")
def change(event):
    alert("Hello !")

configuracoes = {
    "identar": document["identar-checkbox"].checked, #@param {type:"boolean"}
    "espacos_identacao": int(document["espacos-input"].value), #@param {type:"integer"}
    "ordenar": document["ordenar-checkbox"].checked, #@param {type:"boolean"}
    "somente_ascii": document["somente-ascii-checkbox"].checked, #@param {type:"boolean"}
    "dicionario": "{'result': {'country': {'long_name': 'Brasil', 'short_name': 'BR'}, 'state': {'long_name': 'São Paulo', 'short_name': 'SP'}, 'city': {'long_name': 'Ribeirão Preto', 'short_name': 'Ribeirão Preto'}, 'district': None, 'neighborhood': {'long_name': 'Distrito de Bonfim Paulista', 'short_name': 'Distrito de Bonfim Paulista'}, 'street': {'long_name': '9', 'short_name': '9'}, 'slug': '9-distrito-de-bonfim-paulista-ribeirao-preto-sp-brasil', 'geometry': {'location': {'lat': -21.2345726, 'lng': -47.8181069}, 'viewport': {'northeast': {'lat': -21.2332236197085, 'lng': -47.81675791970851}, 'southwest': {'lat': -21.23592158029151, 'lng': -47.81945588029151}}}}}", #@param {type:"string"}
}
document['dict-textarea'].text = configuracoes["dicionario"]

def transformar_dict_em_json(event):
    configuracoes["dicionario"] = eval(document['dict-textarea'].value)
    if configuracoes["identar"]:
        app_json = json.dumps(
            configuracoes["dicionario"],
            indent=configuracoes["espacos_identacao"],
            ensure_ascii=configuracoes["somente_ascii"],
            sort_keys=configuracoes["ordenar"],
            default=str
        )
    else:
        app_json = json.dumps(configuracoes["dicionario"], default=str)

    document['json-textarea'].text = app_json

transformar_dict_em_json(configuracoes)
document["converter-button"].bind("click", transformar_dict_em_json)

# title = 'Python'
# document['header'].html = f"Hello, {title}!"

# counter = 0

# def increment(ev):
#     global counter
#     counter += 1
#     document['counter'].html = str(counter)

# document["converter-button"].bind("click", increment)

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
